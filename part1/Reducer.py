#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass

#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


top3_dict_ip_count = [(i[7:],dict_ip_count[i]) for i in sorted(dict_ip_count,key = lambda x: dict_ip_count[x],reverse = True)[0:3]]

for ip, count in top3_dict_ip_count:
    print ('%s\t%s' % (ip, count))

