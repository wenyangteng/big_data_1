#!/usr/bin/env python
# coding: utf-8

import sys
import collections
from operator import itemgetter
res = collections.defaultdict()

for line in sys.stdin:
    line = line.strip(str)
    time, num = line.split('\t')
    res[time] += 1

top3_res = sort(res.iteritems(), key = operator.itemgetter(1), reverse = True)[:3]

for time, num in top3_res:
    print ('%s\t%s' % (time, num))

     
    
