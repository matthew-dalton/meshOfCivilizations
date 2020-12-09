###############################################################################
# File name     : reduce_location.py
# Created by    : Bogdan State
# Creation date : June 9th, 2013
# Last modified : June 9th, 2013
# Description   : counts how many connections between a pair of two countries
###############################################################################

import sys
current_key=""
current_count = 0

for line in sys.stdin:
	[key, value] = line.strip().split("\t")
	key_list = key.split(",")
	if key_list[0] > key_list[1]:
		key = key_list[1] + "," + key_list[0]
	if key!=current_key:
		if current_key!="":
			print current_key+"\t"+str(current_count)
		current_key = key
		current_count = 0
	current_count = current_count + int(value)
