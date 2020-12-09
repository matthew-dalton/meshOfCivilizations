#########################################################
# File: build_location_dict.py													#
# Created: June 09, 2013																#
# Modified: June 09, 2013																#
# Author: Bogdan State																	#
# Description: Constructs dictionary mapping            #
#   user to location                                    #
#########################################################

import csv
import cPickle as pickle

FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"
TXT_FILE_NAME = "location_iso2c.txt"
PKL_FILE_NAME = "location_iso2c.pkl"

location_dict = {}
with open(FILE_LOCATION+TXT_FILE_NAME, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		location_dict[row[0]] = row[1]

output = pickle.Pickler(open(FILE_LOCATION + PKL_FILE_NAME, 'wb'))
output.fast = True
output.dump(location_dict)
