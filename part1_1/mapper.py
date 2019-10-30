#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys
pat = re.compile('(?P<time>\d\d\d\d)(?P<tag>\D)')
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    for i in line:
        match = pat.search(i)
        if match:
            hr = int(match.group("time")[:2])
            mnt = int(match.group("time")[2:])
            if match.group("tag") == 'P':
                hr += 12
            print('%s\t%s' % ('[' + str(hr) + ':' + str(mnt) + ']', 1))
