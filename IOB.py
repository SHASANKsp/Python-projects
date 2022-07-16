
#Assignment IOB
#Files downloaded from nextprot database

# Q1
#counting number of protein
count = 0
#creating an empty dictionary to store the values
dict={}
#reading the file
file1= open(r'C:\Users\SHASANK SHEKHAR PADH\Desktop\IoB\nextprot_all.peff', 'r')
label=""

for line in file1:
    if '>' in line:
        #reading the header file
        count += 1
        label = line
        #saving acession no. as the key of the dict
        dict[label.split()[0]]= ""
    else:
        dict[label.split()[0]] += line.strip('\n')
        #saving the protein sequence as values
    

print("Number of protein sequence in the file:",count)
print("\n Protein accession no:", "Length of protein")

for key in dict:
    print(key, ":", len(dict[key]))

#Q2
#reading the file
file1= open(r'C:\Users\SHASANK SHEKHAR PADH\Desktop\IoB\nextprot_all.peff', 'r')

dictpe={}
#applying PE=5 filter
for line in file1:
    if ">" in line:
        if "\PE=5" in line:
            dictpe[line.split()[0]]= dict[line.split()[0]]
           
#print(dictpe)
filenew = open(r'C:\Users\SHASANK SHEKHAR PADH\Desktop\IoB\PE_Segregated_070118.fasta', "w")

for key in dictpe:
  filenew.write(key + "\n" + dict[key] + "\n\n")
filenew.close()



#Q3

lst = []
dictf = {}
for key in dictpe:
    x=[]
    lst.append(dictpe[key])
    for seq in lst:
        a=0
        for i in range(a,len(seq)-1):
            if seq[i]=="K" or seq[i]=='R':
                if seq[i+1]!="P" and len(seq[a:i+1]) <= 35 and len(seq[a:i+1]) >=7  :
                    x.append(seq[a:i+1])
                    #print(x)
                    dictf[key] = x
                    a=i+1

# print(dictf)

filenew = open(r'C:\Users\SHASANK SHEKHAR PADH\Desktop\IoB\PE_Segregated_peptide.txt', "w")

for key in dictf:
    filenew.write(key + "\t")
    m = len(dictf[key])
    filenew.write(str(m))
    filenew.write("\t")
    for i in dictf[key]:
        filenew.write(i)
        filenew.write(";")
    filenew.write("\n")
filenew.close()
