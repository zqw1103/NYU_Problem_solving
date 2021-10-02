#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
def gene_gid_exon(data):
    with open("/Users/zunqiuwang/Bioinfo assignments/CCDS.current.txt", "r") as data:
        reader = csv.DictReader(data, delimiter="\t")
        out = open("/Users/zunqiuwang/Desktop/gene_gid_exons1.txt", 'w')
        out.write('Gene'+'\t'+'Gene ID'+'\t'+ 'cds_locations'+'\n')
        for row in reader:
            out.write(row['gene']+'\t'+row['gene_id']+'\t'+row['cds_locations']+'\n')
    out.close()
    return out


# In[4]:


gene_gid_exon(data)


# In[ ]:




