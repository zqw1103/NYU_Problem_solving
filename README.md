# NYU_Problem_solving

Accessing Sequence Data and Performing an MSA

# Create a Biopython session and save a list of Spike protein fasta sequences. Run it to collect files containing fasta sequences. I obtained 1000 sequences with the 'retmax' parameter of the esearch method.   Minimum retmax is 200 fasta sequences.

# Download Clustal Omega and use Python's OS module to run command line arguments to execute MSA on each fasta file. I aligned 1000 sequences in eight minutes, minimum retmax is 200 fasta sequences.. My machine has 32 gb of ram. If you have 16gb then it should align in under 20 minutes.

# Access the 'pubmed' database and return 10 articles about the spike protein. Reading the articles is

# up to you.

# Determine which protein family the Spike protein is a member of.

# Look for any variation between the fasta protein sequences.

# BONUS: Determine gene ontology data via GO

# Determine the part of the spike that binds to the ACE2 receptor. Get a list of 200 fasta sequences and run an msa.

# Access KEGG to get genome information on 'SARS-CoV-2'. Use ID to get the COVID-19 description(COVID-19 [DS:H02398]). From here access all network data for Spike protein, 'S'.

# Use hsa(homo sapiens) # and kgml to get the pathway image file.

# Additional information such as pathways that 'SARS-CoV-2/COVID-19' participate in.

# What's the relationship between the ACE2 of Renin-angiotensin system and 'SARS-CoV-2/COVID-19'?