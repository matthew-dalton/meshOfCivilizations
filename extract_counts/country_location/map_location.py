###############################################################################
# File name     : map_location.py
# Created by    : Bogdan State
# Creation date : June 9, 2013
# Last modified : June 9, 2013
# Description   : Takes tweet connections and maps their location
###############################################################################

import pickle
import sys

FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"
PKL_FILE_NAME = "location_iso2c.pkl"

location_dict = pickle.load(open(FILE_LOCATION + PKL_FILE_NAME, 'rb'))

for row in sys.stdin:
	[first, second] = row.strip().split(sys.argv[1])
	try:
		first = location_dict[first]
		second = location_dict[second]
		print row.strip()+","+first+","+second
	except:
		pass
