#!/usr/bin/env python
# coding: utf-8

import sys
import operator

hash_location = {}

for line in sys.stdin:
    line = line.strip()
    location, count = line.split('\t')
    hash_location[location]= hash_location.get(location,0)+ count
    
top_location = sorted(hash_location.items(), key=operator.itemgetter(1),reverse = True)[0]

print ('%s\t%d'% (top_location[0], top_location[1]))

     
    
