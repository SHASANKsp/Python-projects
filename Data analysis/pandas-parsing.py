import pandas as pd


print("hi")

x=pd.read_csv("F:/Software bioinfo/GIT dir/Python-Biopython/DA/Genome Glossary.csv")
#print (x)
#help(pd.read_csv)
x.to_csv("F:/Software bioinfo/GIT dir/Python-Biopython/DA/test_out.csv",index = "FALSE")
y = pd.read_csv("F:/Software bioinfo/GIT dir/Python-Biopython/DA/test_out.csv")
#print(y)

a = pd.read_excel("F:/Software bioinfo/GIT dir/Python-Biopython/DA/test_out.xlsx",sheet_name="test_out")
print(a)
a.to_excel("F:/Software bioinfo/GIT dir/Python-Biopython/DA/new_test_out.xlsx",sheet_name="yessssss")



#-----------------------------------------------------------------------------------------><
