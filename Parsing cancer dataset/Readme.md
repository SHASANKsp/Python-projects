A. Opening the protein FASTA file and print the number of sequences and length of each protein sequences. Print the output in following format:

Number of protein sequences in file: NN

1. Protein accession: Length of the protein

2. Protein accession: Length of the protein


B. Segregate protein sequences with tag “PE=5” in the header and store them in separate file with name “PE_Segregated_070118.fasta”

C. Open file “PE_Segregated_070118.fasta” and generate peptides using following criteria:

a) Peptide should end with either “K” or “R”

b) “K” or “R” should not be succeeded by “P”

c) Length of the peptides should be ≥ 7 and ≤ 35 amino acids

Store the result in tab-delimited format in separate file in following scheme: Protein accession Number of peptides List of peptides separated by “;”

For example, if the protein sequence is ASPRSTRSKGIWMNVCDSRPEWRQDFG

The peptides will be

ASPR

STR

SK

GIWMNVCDSRPEWR

QDFG
