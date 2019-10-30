#!/usr/bin/python
import sys
import collections
from operator import itemgetter
res = collections.defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    time, num = line.split('\t')
    res[time] += 1

top3_res = sorted(res.items(), key = itemgetter(1), reverse = True)

for time, num in top3_res[:3]:
    print ('%s\t%s' % (time, num))
