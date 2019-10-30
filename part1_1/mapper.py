#!/usr/bin/python
# --*-- coding:utf-16 --*--

import re
import sys
import codecs
pat = re.compile('(?P<time>\d\d\d\d)(?P<tag>\D)')
utf16reader = codecs.getreader("utf_16")
sys.stdin = utf16reader(sys.stdin)
for line in sys.stdin:
    line = line.split(',')[19]
    match = pat.search(line)
    if match:
        hr = int(match.group("time")[:2])
        mnt = int(match.group("time")[2:])
        if match.group("tag") == 'P':
            hr += 12
        print('%s\t%s' % ('[' + str(hr) + ':' + str(mnt) + ']', 1))
