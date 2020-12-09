#########################################################
# File: build_location_dict.py													#
# Created: June 09, 2013																#
# Modified: June 09, 2013																#
# Author: Bogdan State																	#
# Description: Constructs dictionary mapping            #
#   user to degree                                      #
#########################################################

import csv
import cPickle as pickle

FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"
TXT_FILE_NAME = "twitter_bidirected_deg.txt"
PKL_FILE_NAME = "twitter_bidirected_deg.pkl"

dictionary = {}
with open(FILE_LOCATION+TXT_FILE_NAME, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		dictionary[row[0]] = row[1]

output = pickle.Pickler(open(FILE_LOCATION + PKL_FILE_NAME, 'wb'))
output.fast = True
output.dump(dictionary)
