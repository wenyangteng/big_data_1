#!/usr/bin/python
import sys
import collections
from operator import itemgetter
res = collections.defaultdict()

for line in sys.stdin:
    line = line.strip()
    time, num = line.split('\t')
    res[time] += 1

top3_res = sorted(res.items(), key = itemgetter(1), reverse = True)[:3]

for time, num in top3_res:
    print ('%s\t%s' % (time, num))

     
    
