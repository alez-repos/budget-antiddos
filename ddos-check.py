#!/usr/bin/python

from itertools import groupby
from warnings import filterwarnings
filterwarnings( action="ignore")
from ipwhois import IPWhois
import sys

# we allow this number of connections from same /24 range
threshold = 2
# show ipwhois info
showipw = True

file1 = open('m0.filtered', 'r') 
Lines = file1.readlines() 
  
#count = 0
#for line in Lines: 
#    line = line.strip() 
#    print("Line {}: {}".format(count, line)) 
#    count = count + 1

my_list = Lines

each_word = sorted([x.strip().split(".") for x in my_list])

grouped = [list(value) for key, value in groupby(each_word, lambda x: x[:-1])]

result = []
for group in grouped:
    temp = []
    for i in range(len(group)):
        temp.append(".".join(group[i]))
    result.append(temp)

for range in result:
    if len(range) > threshold:
        esub = range[0].split(".")
        toblock = esub[0]+"."+esub[1]+"."+esub[2]
	if showipw == True:
            obj = IPWhois(toblock+".0")
            ext = obj.lookup_whois()
            print("RANGE: {} \t DIFFERENT IPS: {} \t COUNTRY: {} \t ASN: {}".format(toblock,len(range),ext['asn_country_code'],ext['asn_description'])) 
	    print(range)
	else:
	    print("RANGE: {} \t DIFFERENT IPS: {}".format(toblock,len(range)))
	    print(range)

for range in result:
    if len(range) > threshold:
	esub = range[0].split(".")
	toblock = esub[0]+"."+esub[1]+"."+esub[2]
	print("iptables -I INPUT 1 -s {}.0/24 -j DROP".format(toblock))


