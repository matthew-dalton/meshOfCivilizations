export location="[twitter_location]"
R CMD BATCH location_ISO.R
python build_location_dict.py
cat $location/AllLinks.txt | python country_location/map_location.py > $location/links_iso2c.txt
cat $location/links_iso2c.txt | sort -k 1,1 -T $location > $location/links_iso2c_sorted.txt
cat $location/links_iso2c_sorted.txt  | python country_location/reduce_location.py > twitter_counts.txt

### Count bidirected ties
cat $location/AllLinks.txt | python bidirected/mapper.py | sort -k1,1 -T $location | python bidirected/reducer.py > $location/links_bidirected.txt
cat $location/links_bidirected.txt | python country_location/map_location.py , > $location/links_bidirected_iso2c.txt
cat $location/links_bidirected_iso2c.txt | sort -k 1,1 -T $location | python country_location/reduce_location.py > twitter_bidirected_counts.txt
cat $location/links_bidirected.txt | python num_connections/mapper.py , | sort -k 1,1 -T $location | python num_connections/reducer.py > $location/twitter_bidirected_deg.txt
cat $location/twitter_bidirected_deg.txt | python deg_dist/mapper.py , | sort -k 1,1 -T $location | python deg_dist/reducer.py > twitter_bidirected_degdist.txt
python build_degree_dict.py
cat $location/links_bidirected.txt | python filter_min_degree/mapper.py , 1000 | sort -k 1,1 -T $location > $location/twitter_bidirected_mindeg.txt
cat $location/twitter_bidirected_mindeg.txt | python country_location/map_location.py , > $location/twitter_bidirected_mindeg_location.txt

# Count ties / country pair
cat $location/twitter_bidirected_mindeg_location.txt | cut -f 3,4 -d , | awk '{print $0 "\t" 1}' | 
  python country_location/reduce_location.py | sort -k 1,1 -T . | 
  python country_location/reduce_location.py > twitter_bidirected_mindeg_counts.txt

# Count users / country
{ cat $location/twitter_bidirected_mindeg_location.txt | cut -f 1,3 -d , ; 
{ cat $location/twitter_bidirected_mindeg_location.txt | cut -f 1,3 -d , ; cat $location/twitter_bidirected_mindeg_location.txt | cut -f 2,4 -d , ; } | 
	sort | uniq | cut -f 2 -d , | awk '{print $0 "\t" 1}' | sort | python country_location/reduce_location.py > twitter_bidirected_mindeg_penetration.txt


# Assign unique identifiers to users
{ cat $location/twitter_bidirected_mindeg.txt | cut -f 1 -d , ; cat $location/twitter_bidirected_mindeg.txt | cut -f 2 -d , ; } | 
				sort -T $location | uniq | awk '{print $0 "," NR}' > $location/twitter_bidirected_unique_users.txt
join -1 1 -2 1 
		 -o 0,1.2,2.2
     < (cat $location/twitter_bidirected_mindeg.txt) \
    < (cat $location/twitter_bidirected_unique_users.txt)
