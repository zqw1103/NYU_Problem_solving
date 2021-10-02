#!/usr/bin/env python
# coding: utf-8

# In[2]:


with open("/Users/zunqiuwang/Desktop/CCDS.current.txt", "r") as f:
    out = open("/Users/zunqiuwang/Desktop/gene_gid_exons2.txt", 'w')
    out.write('Gene'+'\t'+'Gene ID'+'\t'+ 'cds_locations'+'\n')
    for line in f:
        data = line.split('\t')
        if 'public' and '+' in line: 
            out.write(data[2] +'\t'+ data[3] + '\t' + data[9]+'\n')
out.close()


# In[ ]:





# In[ ]:




