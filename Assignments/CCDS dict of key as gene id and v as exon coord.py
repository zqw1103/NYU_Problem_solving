#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
with open("/Users/zunqiuwang/Desktop/CCDS.current.txt", "r") as f:
    out = open("/Users/zunqiuwang/Desktop/gene id and coord.txt", 'w') 
    dict_id={}
    for line in f:
        x = line.split('\t')
        if 'Public' in line: 
            dict_id[x[3]] = x[9]
    out.write(str(dict_id))


# In[ ]:




