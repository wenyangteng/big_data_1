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

for line in sys.stdin::
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass
    

def top3_ip(x):
    x = input("Please print the time period you want to search, such as 0-1")
    time_period = x[0]
    temp0 = {}
    for key in dict_ip_count:
        if key[2] == x:
            temp0[key]=dict_ip_count[key]
    top3_dict_ip_count = [(i[7:],dict_ip_count[i]) for i in sorted(temp0,key = lambda x: temp0[x],reverse = True)[0:3]]
    for ip, count in top3_dict_ip_count:
        print ('%s\t%s' % (ip, count))
 top3_ip(x)

