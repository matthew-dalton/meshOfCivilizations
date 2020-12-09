#########################################################
# File: location_ISO.R																	#
# Created: June 09, 2013																#
# Modified: June 09, 2013																#
# Author: Bogdan State																	#
# Description: Extracts ISO-2167-2 codes for countries  #
#########################################################

FILE.LOCATION = "/media/bogdan/61ec6432-da13-415d-9afd-fd46e933f48b/twitter"
FILE.NAME = "location.txt"
NEW.FILE.NAME = "location_iso2c.txt"
library("data.table")
library("countrycode")

locations = fread(paste(FILE.LOCATION,FILE.NAME,sep="/"), sep="|", verbose=T) 
system.time(
locations[,country:=countrycode(V2,"country.name","iso2c")]
)
locations[,V2:=NULL]

tbl.twitter.users.country <- table(locations$country)
countries.gt.1000 <- names(tbl.twitter.users.country)[tbl.twitter.users.country > 1000]
save(tbl.twitter.users.country, countries.gt.1000, file="twitter.users.RData")

write.csv(locations, file=paste(FILE.LOCATION, NEW.FILE.NAME, sep="/"), row.names=F, quote=F)
