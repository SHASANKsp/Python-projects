import matplotlib.pyplot as plt

print("Welcome")
print("The genome size is alwas given as the total amount of DNA contained within one copy of a single genome (1n).")

	#creating a dict for storing the data 
g_size = {"Enterococcus_faecium" : 2736723, "Pseudomonas_aeruginosa" : 6264404, "Thermothielavioids_terrestris" : 10101509, "Aspergillus_fumigatus" : 4918979, "Escherichia_coli" : 4641652, "Arachis_hypogaea" : 112420854, "Brassica_napus" : 35822559, "Arabidopsis_thaliana" : 30427671, "Capsicum_annuum" : 301019445, "Drosophila_melanogaster" : 23542271, "Chrysomallon_squamiferum" : 49218974, "Physeter_catodon" : 145741392, "Danio_rerio" : 59578282, "Rattus_norvegicus" : 282763074, "Homo_sapiens" : 248956422}
print(g_size)

genome_size = g_size.values()
#genome_size = [2736723, 6264404, 10101509, 4918979, 4641652, 112420854, 35822559, 30427671, 301019445, 23542271, 49218974, 145741392, 59578282, 282763074, 248956422]
print(genome_size)
print(max(genome_size))

    #creating bins for the histogram
bins = []

for i in range(0,max(genome_size),10000000):
    bins.append(i)

buffer = i + 10000000
bins.append(buffer)

print(bins)

    #creating the histogram
plt.hist(genome_size, bins, histtype= 'bar', rwidth=0.7 )
plt.xlabel('Range of Genomic size(in base pairs)')
plt.ylabel('Frequency of the species in the range')
plt.title('Frequency distribution of the collected genome into their respective ranges')
plt.show()
