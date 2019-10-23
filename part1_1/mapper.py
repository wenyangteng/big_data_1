#!/usr/bin/env python
# coding: utf-8

# When are tickets most likely to be issued?
import re
import sys
pat = re.compile('(?P<time>\d\d\d\d)(?P<tag>\D)')
for line in sys.stdin:
    match = pat.find(line)
    if match:
        hr = int(match.group(time)[:2])
        mnt = int(match.group(time)[2:])
        if match.group(tag) == 'P':
            hr += 12
        print('%s/t%s' % ('[' + str(hr) + ':' + str(mnt) + ']', 1))
