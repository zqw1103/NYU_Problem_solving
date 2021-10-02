#!/usr/bin/env python
# coding: utf-8

# In[34]:


import re
with open("/Users/zunqiuwang/Bioinfo assignments/CCDS.current.txt", "r") as f:
    out = open("/Users/zunqiuwang/Desktop/gene_gid_exons5.txt", 'w')
    out.write('Gene'+'\t'+'Gene_ID'+'\t'+ 'cds_locations'+'\n')
    for line in f:
        data = line.split('\t')
        num = re.findall('\d*[-]\d+', data[9])
        if len(num) > 4:
            out.write(data[2] +'\t'+ data[3] + '\t' + data[9]+'\n')
out.close()


# In[ ]:




