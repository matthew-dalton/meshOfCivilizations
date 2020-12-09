###############################################################################
# File name     : reducer.py
# Created by    : Bogdan State
# Creation date : June 11th, 2013
# Last modified : June 11th, 2013
# Description   : counts how followers a Twitter user has
###############################################################################

import sys
current_key=""
current_count = 0

for line in sys.stdin:
	[key, value] = line.strip().split("\t")
	if key!=current_key:
		if current_key!="" and current_count > 1:
			print current_key
		current_key = key
		current_count = 0
	current_count = current_count + int(value)
