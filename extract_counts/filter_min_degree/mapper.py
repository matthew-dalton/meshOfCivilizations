###############################################################################
# File name     : map_location.py
# Created by    : Bogdan State
# Creation date : June 9, 2013
# Last modified : June 9, 2013
# Description   : Takes tweet connections and maps their location
###############################################################################

import pickle
import sys

THRES = int(sys.argv[2])
FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"

PKL_FILE_NAME = "twitter_bidirected_deg.pkl"
degree_dict = pickle.load(open(FILE_LOCATION + PKL_FILE_NAME, 'rb'))


for row in sys.stdin:
	[first, second] = row.strip().split(sys.argv[1])
	try:
		if int(degree_dict[first]) < THRES and int(degree_dict[second]) < THRES:
			print first+","+second
	except:
		pass
