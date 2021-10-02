#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
def gene_gid_exons(data):
    data = open("/Users/zunqiuwang/desktop/CCDS.current.txt", "r")
    reader = csv.reader(data, delimiter="\t")
    ccds=list(reader)
    out = open("/Users/zunqiuwang/Desktop/gene_gid_exons.txt", 'w')
    for i in range(len(ccds)):
        out.write(ccds[i][2]+'\t'+ccds[i][3]+'\t'+ccds[i][9]+'\n')
    return out
gene_gid_exons(data = open("/Users/zunqiuwang/desktop/CCDS.current.txt", "r"))


# In[ ]:




