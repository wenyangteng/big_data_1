#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys
pat = re.compile('(?P<time>\d\d\d\d)(?P<tag>\D)')
for line in sys.stdin:
    line = line.split('\t')[19]
    match = pat.search(line)
    if match:
        try:
            hr = int(match.group("time")[:2])
            mnt = int(match.group("time")[2:])
            if match.group("tag") == 'P':
                hr += 12
            print('%s\t%s' % ('[' + str(hr) + ':' + str(mnt) + ']', 1))
        except:
            pass
