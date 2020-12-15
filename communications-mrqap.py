import csv
import numpy as np

from libs.mrqap import MRQAP

###########################################
# MAP COUNTRIES AND THEIR CODES TO THEIR INDEX
# (array index is the mapping for 'countries')
###########################################

# create mapping from country name to row
# only consider countries with more than 5mil population

countries = []
code_index_map = {}
with open("data/codes_over_5mil.csv") as f:
    reader = csv.reader(f, delimiter=" ")
    next(reader)  # skip titles
    i = 0
    for row in reader:
        countries.append(row[1])
        code_index_map[row[2]] = i
        i += 1

size = len(countries)


# helper function
def same_alliance(list1, list2):
    for alliance in list1:
        if alliance in list2:
            return True

    return False

###########################################
###########################################
# COLLECT INDEPENDENT VARIABLES
###########################################
###########################################

###########################################
# CREATE CONTINENT MATRIX
###########################################


# create mapping from country to continent
countries_to_continents = {}
with open("data/Countries-Continents.csv") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip titles
    for row in reader:
        countries_to_continents[row[1]] = row[0]

# create square matrix where:
#   entry is 1 if countries share a continent
#   entry is -1 if they do not
continent_matrix = np.zeros((size, size))

# fill in matrix row by row
for i in range(size):

    country_i = countries[i]
    for j in range(size):

        country_j = countries[j]
        continent_matrix[i, j] = 1 if countries_to_continents[country_i] == countries_to_continents[country_j] else -1

###########################################
# CREATE G20 & G33 MATRIX
###########################################

# create mapping from country to alliances
countries_to_alliances = {}
with open("data/Country-Alliance.csv") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        if row[0] in countries_to_alliances.keys():
            countries_to_alliances[row[0]].append(row[1])
        else:
            countries_to_alliances[row[0]] = [row[1]]


# create square matrix where:
#   entry is 1 if countries share a G20 or G33 alliance
#   entry is -1 if they do not
alliance_matrix = np.zeros((size, size))

# fill in matrix row by row
for i in range(size):

    country_i = countries[i]
    for j in range(size):

        country_j = countries[j]
        if not (country_i in countries_to_alliances.keys() and country_j in countries_to_alliances.keys()):
            same = False
        else:
            same = same_alliance(countries_to_alliances[country_i], countries_to_alliances[country_j])

        alliance_matrix[i, j] = 1 if same else -1


###########################################
# ASSEMBLE INDEPENDENT VARIABLE DICTIONARY
###########################################

independents = {
    "CONTINENT_AFFILIATION": continent_matrix,
    "ALLIANCE_AFFILIATION": alliance_matrix,
}

###########################################
###########################################
# COLLECT DEPENDENT VARIABLE
###########################################
###########################################

# create mapping from country code pair to communication density
code_pairs_to_densities = {}
with open("data/dij_joint_civ.csv") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        pair = row[0] + "," + row[1]
        code_pairs_to_densities[pair] = row[2]


# create a square matrix where:
#   entries are computed communication densities between countries
density_matrix = np.zeros((size, size))

# fill in matrix row by row
for key in code_pairs_to_densities:

    pair = key.split(",")

    # assert both countries have sufficient population size for study
    if not (pair[0] in code_index_map.keys() and pair[1] in code_index_map.keys()):
        continue

    i = code_index_map.get(pair[0])
    j = code_index_map.get(pair[1])

    # put densities into matrix
    density_matrix[i, j] = code_pairs_to_densities.get(key)
    density_matrix[j, i] = code_pairs_to_densities.get(key)

dependents = {
    "COMMUNICATION_DENSITY": density_matrix,
}

###########################################
###########################################
# PERFORM MRQAP
###########################################
###########################################

NPERMUTATIONS = 2000

mrqap = MRQAP(Y=dependents, X=independents, npermutations=NPERMUTATIONS, diagonal=False, directed=False)
mrqap.mrqap()
mrqap.summary()