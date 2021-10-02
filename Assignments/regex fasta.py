#!/usr/bin/env python
# coding: utf-8

# In[25]:


x = """>gi|27544883|ref|NP_775396.1| putative ribosomal protein S3 (mitochondrion) [Lecanicillium muscarium]
MEKNIKLKNILLSKVPQKITLNNKIADIRKTKYLPSFSKEWKDTIYSYNKNIMKNIPSHHLNINKIIQSYFNLFFSTNKN
NQNKRFISFGKYITMKRRRNLLRKIYVSNPVFKFSYFSAFITLFSLSREKVFYKKNILKRIKKYKVIKCNVIYFYIKIIK
WIYKIFLAKQYYKNKNISYFLLKNKNKFIQYKLKYLSKFLLLKNLYLKRVWSKIIKNFIKRHLIFLRKYELLYSLNQLKF
NKLTLLNKLSLLLNKILGKKIEYNIINLKSIIFNSDLFTQAITLKFQKRKSFNYKKNILSILGRVNFPYFKDVVALAYNE
STNYILNKYKDGKILSYINNHQNLDNFINKIHNATNKNIHKEIFNSIQYKNIEGIRIETNGRLTKRYRADRAVHYRKWKG
GLQKTSLNSTLFRGNVNPNISYSIVNNTRRVGSFAIRGWISGK
>gi|27544884|ref|NP_775397.1| NADH dehydrogenase subunit 2 (mitochondrion) [Lecanicillium muscarium]
MIIISILSLLLSNAVNLRRDVSILYNRIAILILLYCIVHDYTSLTVVTKGIGLHGGLLLINNLTQIFHIFVFIVTIFILT
LTSFYPRKVWVSEYSSIKDLEPVDPLFNKFIYYNTKIINKMGEHLKIIEYPLILLFIVRPGAIFLMSSNDLITIFLSIEL
QSYGLYILSTVYRNSELSTTGGLIYFLLGGLSSCFILLGTALLYAKSGRTSLESLYIITSISDIHSSTNDLWYSPNYISL
SLVIFTVGFLFKISAAPFHFWSPDVYDAIPTIVTTFVALIAKISILILLLQLVYYTNADITMNNWTFILLISSLFTLVIG
TVVGLTQFRIKRLFAYSTISQIGFMLLALSISSIESTQAPIFYLTQYIIINLNAFIILLAITYSLYFYTNYNKEHKDLLD
KTNSPIQLITQLKGYFFINPVLALNLTITIFSFSQIPPLLVCFCKQIVLSASLNQNLYFITLIAILTNFIERIYYLTIIK
KIFFNKSDYKINTLLCNFKLKINIYNNNNSINSVEYNYKNIFLSIPISFIISILTLTILFFLFINKKWLIMITIFVQLIF
NS
>gi|27544885|ref|NP_775398.1| NADH dehydrogenase subunit 3 (mitochondrion) [Lecanicillium muscarium]
MSGTTFLFIFVCVIAILFLALNFILAPHNPYQEKYSIFECGFHSFLGQNRTQFGFKFFIFSLVYLLLDLDLEILVIYPYG
LSSYENGIYGLIIVLLFIGIITAGFVFELGKGALKIDSRQSYNYFNVQSTKNFINTFFENK"""


# In[22]:


def protein_dict(seq):#how to modify code to extrsct definition line using regex
    define_line =[]
    seq_split = seq.split('>')
    seq_split.pop(0)   
    for i in range(len(seq_split)):
        define_line.append(seq_split[i].split('\n')[0])
    return(define_line)


# In[16]:


protein_dict(x) #also want to pass this function to another function using regex to extract gene ID


# In[23]:


def pro_id(define_line):
    import re
    for ID in define_line:
        s = re.finditer(r'\|[0-9]+\|',ID)
        for t in s:
            print(t.group() + ' is located from ' + str(t.start()) + ' to ' + str(t.end()))


# In[24]:


pro_id(protein_dict(x))


# In[52]:


pro_seq = ['gi|27544883|ref|NP_775396.1| putative ribosomal protein S3 (mitochondrion) [Lecanicillium muscarium]',
 'gi|27544884|ref|NP_775397.1| NADH dehydrogenase subunit 2 (mitochondrion) [Lecanicillium muscarium]',
 'gi|27544885|ref|NP_775398.1| NADH dehydrogenase subunit 3 (mitochondrion) [Lecanicillium muscarium]']


# In[120]:


import re
for id in pro_seq:
    s = re.finditer(r'\|[0-9]+\|',id)
    for t in s:
        print(t.group() + ' is located from ' + str(t.start()) + ' to ' + str(t.end()))


# In[34]:


import re 
fasta = re.findall(r'gi.*', x) 
print(fasta)


# In[91]:


import re
for id in pro_seq:
    s = re.finditer(r'\[(\w+) (\w+)\]', id)
    for b in s:
        name = b.group()
        start1 = b.start(0)
        start2 = b.start(1)
        end1 = b.end(0)
        end2 = b.end(1)
        print(name + ' ' + ' has start at ' + str(start1) + ' end at ' + str(end1) + " and " + 'start at ' + str(start2) + ' end at ' + str(end2)) # try to find the gene ID


# In[10]:


import re
for ID in protein_dict(x):
    s = re.search(r'.*\|[0-9]{8}\|$',ID)
    if s:
        print(s)


# In[88]:


mos = re.finditer("[Hh]ello", "Hello world, hello Python,!")
for x in mos:
    print(x.group(0))
    print(x.span(0))


# In[92]:


Eif2b2 = """ Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    pass5
Eif2b2    fail
Eif2b2    pass2
Eif2b2    fail
Eif2b2    pass4
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail
Eif2b2    fail"""


# In[93]:


import re


# In[99]:


extract = re.findall(r'[\s][a-z\d]+', Eif2b2)


# In[100]:


extract2 = [x.strip() for x in extract]


# In[101]:


print(extract2)


# In[102]:


key_value_pairs = {}
for key in extract2:
    
    if key in key_value_pairs:
        
        key_value_pairs[key] += 1
        
    else:
        
        key_value_pairs[key] = 1
        print("Eif2b2 outcomes are fail :", end = " ")        


# In[104]:


printList = [str(key_value_pairs[key]) + " of " + key + "s"              for key in key_value_pairs]
for x in range(len(printList) -1) : print(printList[x], end = ", ")
print(printList[-1], end = ".\n")


# In[ ]:




