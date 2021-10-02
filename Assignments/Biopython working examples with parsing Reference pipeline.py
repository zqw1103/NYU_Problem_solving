#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install biopython


# In[1]:


from Bio import Seq
from Bio import Entrez
from Bio import SeqIO
Entrez.email = 'A.N.Other@example.com'


# In[2]:


handle = Entrez.einfo()


# In[3]:


handle = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", idtype="acc")
record = Entrez.read(handle)
record["idList"]


# In[4]:


#eserch
handle = Entrez.esearch(db="protein", term= "CTLA-4", rettype = 'fasta', retmode = 'xml', retmax=1000)
record = Entrez.read(handle)
record["IdList"]


# In[5]:


CTLA4_id=record["IdList"]
handle = Entrez.efetch(db="protein", id=','.join(CTLA4_id), rettype="fasta", retmode="text")
print(handle.read())


# In[6]:


#afteresearch, efetch and write to file
CTLA4_id=record["IdList"]
handle = Entrez.efetch(db="protein", id=','.join(CTLA4_id), rettype="fasta", retmode="text")

file = "/Users/zunqiuwang/Desktop/CTLA-4 FASTA.fasta"
with open (file,'w') as f:
    f.write(handle.read())
    f.close()


# In[31]:


#SeqIO parse file
CTLA4_record = SeqIO.parse("/Users/zunqiuwang/Desktop/CTLA-4 FASTA.fasta", 'fasta')
for x in CTLA4_record:
    print(x.id)
    print(x.description)
    print(x.seq)


# In[19]:


handle = Entrez.esearch(db="nuccore", term= "CTLA-4", rettype = 'gb', retmode = 'xml')
record = Entrez.read(handle)
record["IdList"]
record["Count"]


# In[166]:


# extract genbank name and seq
CTLA4_id=record["IdList"]
handle = Entrez.efetch(db="nuccore", id=','.join(CTLA4_id), rettype="gb", retmode='txt')
out = open("/Users/zunqiuwang/Desktop/CTLA-4 gb.gbk", 'w')
out.write(handle.read())

out1 = open("/Users/zunqiuwang/Desktop/CTLA-4 name+seq.txt", 'w')
for gb_record in SeqIO.parse(open("/Users/zunqiuwang/Desktop/CTLA-4 gb.gbk", 'r'), 'gb'):
    out1.write("Name %s, %i features, %s" % (gb_record.name, len(gb_record.features), gb_record.seq))


# In[6]:


#esearch CLTA-4 journals
handle = Entrez.esearch(db="pubmed", term='CTLA-4', retmax=1000)
result = Entrez.read(handle)
clta4journalid = result['IdList']


# In[13]:


#efetch CLTA-4 journals
handle = Entrez.efetch(db="pubmed", id=','.join(clta4journalid), rettype='Abstract', retmode='txt')
out1 = open("/Users/zunqiuwang/Desktop/CTLA-4 journals.txt", 'w')
out1.write(handle.read())


# In[ ]:


#afteresearch, efetch and write to file
file = "/Users/zunqiuwang/Desktop/CTLA-4 gb.txt"
with open (file,'w') as f:
    f.write(handle.read())
    f.close()


# In[26]:


CTLA4_record = SeqIO.parse("/Users/zunqiuwang/Desktop/CTLA-4 gb.gbk", 'gb')

all_species = [seq_record.annotations["source"] for seq_record in SeqIO.parse("/Users/zunqiuwang/Desktop/CTLA-4 gb.gbk", "gb")]
print(all_species)


# In[20]:


CTLA4_id=record["IdList"]
handle = Entrez.efetch(db="nuccore", id=','.join(CTLA4_id), rettype="gb", retmode='txt')
out = open("/Users/zunqiuwang/Desktop/CTLA-4 gb.txt", 'w')
out.write(handle.read())


# In[102]:


#list record
list_CTLA4_record = list(SeqIO.parse("/Users/zunqiuwang/Desktop/CTLA-4 gb.txt", 'gb'))
print(list_CTLA4_record)


# In[128]:


#parse journals from seqIO record
import re
output = open("/Users/zunqiuwang/Desktop/CTLA-4 journal list with seq.txt", 'w')
seq_records = SeqIO.parse("/Users/zunqiuwang/Desktop/CTLA-4 gb.txt", 'gb' )
seq = seq_record.seq
for seq_record in seq_records:
    for i in range(len(seq_record.annotations['references'])):
        title = seq_record.annotations['references'][i].title
        journal = seq_record.annotations['references'][i].journal
        seq = seq_record.seq
        print(title + '\n' + journal + '\n' + str(seq) + '\n')
        output.write(title + '\n' + journal + '\n' + str(seq) + '\n')


# In[27]:


for x in CTLA4_record:
    print(x.id)
    print(x.description)
    print(x.seq)
    print(x.features)


# In[24]:


from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")


# In[25]:


from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)


# In[29]:


E_VALUE_THRESH = 0.04
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("sequence:", alignment.title)
            print("length:", alignment.length)
            print("e value:", hsp.expect)
            print(hsp.query[0:75] + "...")
            print(hsp.match[0:75] + "...")
            print(hsp.sbjct[0:75] + "...")


# In[ ]:


# esearch based on what info i want to query from db and get iDList
# efetch from db(protein, snp,nucleotide,pubmed,structure) based on idList(id=','.join(PD1_snp_list=record['idList'])) to download specific info such as seq, source etc with specified rettype(fasta,uilist, gb,xml,acc), with retmode(text,xml)

