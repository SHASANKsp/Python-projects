from Bio import SeqIO 
#from Bio.SeqIO import parse (Bio.SeqIO.parse() returns an iterator which can only be read through a for loop, and is used when there are more then one sequence in the file)
from Bio.SeqIO import read #read() is for file containing only one sequence different then parse
from Bio.SeqRecord import SeqRecord 


#First phase
#Aim is to parse the fasta file and extract the sequence out alonge with other details in two different variable for the further use.
print('Welcome to the ORF finder \n')
file_path = input('Give path of the .fasta file in the system:\nNote: Do not forget to add the file name at the end of the path \n')
#file_path = ('F:/Software bioinfo/GIT dir/Python-Biopython/my/ORF/pten test.fasta')
file = open(file_path)
my_file = read(file, "fasta")

Seq_ID = my_file.id
Seq_seq = my_file.seq
Seq_len = len(my_file.seq)


#second phase
#since there is only one start codon and three stop codon we are not taking any input about this and going for all stop codon.
#start:ATG 
#stop: TAA TAG TGA

def startc(SEQ):
    ln = len(SEQ)
    start_codon = []
    for i in range(0,ln,3):
        if (SEQ[i]=="A" and SEQ[i+1]=="T" and SEQ[i+2]=="G"):
            start_codon.append(i)
    
    return start_codon

def endc(SEQ):
    ln = len(SEQ)
    end_codon = []
    for i in range(0,ln,3):
        if (SEQ[i]=="T" and SEQ[i+1]=="A" and SEQ[i+2]=="A"):
            end_codon.append(i)
        if (SEQ[i]=="T" and SEQ[i+1]=="A" and SEQ[i+2]=="G"):
            end_codon.append(i)
        if (SEQ[i]=="T" and SEQ[i+1]=="G" and SEQ[i+2]=="A"):
            end_codon.append(i)
    
    return end_codon


#third phase
#convert the seq into six reading frame(3normal and 3reverse)
f11 = Seq_seq 
f12 = Seq_seq[1:]
f13 = Seq_seq[2:]
f21 = Seq_seq[Seq_len::-1] #reversed sequence
f22 = f21[1:]
f23 = f21[2:]


sc11 = startc(f11)
ec11 = endc(f11)
sc12 = startc(f12)
ec12 = endc(f12)
sc13 = startc(f13)
ec13 = endc(f13)
sc21 = startc(f21)
ec21 = endc(f21)
sc22 = startc(f22)
ec22 = endc(f22)
sc23 = startc(f23)
ec23 = endc(f23)
print(sc11,ec11)


