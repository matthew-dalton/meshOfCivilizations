###############################################################################
# File name     : mapper.py
# Created by    : Bogdan State
# Creation date : June 9, 2013
# Last modified : June 11, 2013
# Description   : Counts Bidirected tweets
###############################################################################

import pickle
import sys
import math

FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"

for row in sys.stdin:
	[first, second] = row.strip().split("\t")
	try:
		first = int(first)
		second = int(second)
		min_id = min([first, second])
		max_id = max([first, second])
		tie_id = str(min_id)+","+str(max_id)
		print tie_id+"\t1"
	except:
		pass
