###############################################################################
# File name     : mapper.py
# Created by    : Bogdan State
# Creation date : June 9, 2013
# Last modified : June 9, 2013
# Description   : Takes tweet connections and counts followers
###############################################################################

import pickle
import sys

FILE_LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter/"

for row in sys.stdin:
	[first, second] = row.strip().split(sys.argv[1])
	try:
		print second+"\t1"
	except:
		pass
