#!/usr/bin/env python
# coding: utf-8

# In[16]:


from bioservices import *
b = BioMart(verbose=False)
b.host ='www.ensembl.org'
b.registry()


# In[17]:


b.lookfor('snp')


# In[3]:


b.names


# In[13]:


datasets = b.datasets('ENSEMBL_MART_ENSEMBL')
for s in datasets:
    if 'hsa' in s:
        hsa = s
        print(hsa)
        b.add_dataset_to_xml(hsa)
        hsa_gene = b.attributes(hsa)
        for k,v in hsa_gene.items():
            print(str(k) + '--->' + str(v))
        #hsa_gene_k = hsa_gene.keys() #get attribute name list of dataset(dict key)
        #print(hsa_gene_k)
        #print(b.attributes(s)['pdb'])
        #print(b.attributes(s)['entrezgene_id'])
        #hsa_gene_filter = b.filters(s)
        #print(hsa_gene_filter)
        #hsa_gene_filter_k = hsa_gene_filter.keys()
        #print(hsa_gene_filter_k) #choose what to filter as 1st arg
        #print(b.filters(s)['source']) #choose what to filter as 2nd argument
        #b.add_attribute_to_xml('cdna')
        #b.add_filter_to_xml('source', 'ensembl_havana')
        #xml = b.get_xml()
        #print(xml)
        #res = b.query(xml)
        #print(len(res))
        #res = res.split('\n')
        #for x in res[0:20]:
            #print(res)
        


# In[ ]:




