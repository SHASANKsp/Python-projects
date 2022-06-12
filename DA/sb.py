import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
#sns.displot(data = tips['total_bill'], kde = "TRUE")
#help(sns.displot)
#plt.show()

#-------------------->
#sns.jointplot(x="total_bill",y= "tip",data=tips,kind="kde")
#plt.show()

#--------------------->
#sns.pairplot(tips,hue='sex',palette="coolwarm")

#--------------------->kernal dist. (kde)
#sns.kdeplot(tips['total_bill'])

#---------------------->
#sns.rugplot(tips['total_bill'])

#----------------------------------------------------------------------------------------------------><CATEGORICAL PLOTS
#bar plot
#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

#count plot
#sns.countplot(x='sex',data=tips)

#box plot
#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

#violin plot
#sns.violinplot(x='day',y='total_bill',data=tips)

#STRIP PLOT
#sns.stripplot(x='day',y='total_bill',data=tips)

#swarm plot
#sns.swarmplot(x='day',y='total_bill',data=tips,color="black")

#factor plot
#sns.factorplot(x='day',y='total_bill',data=tips,kind="bar")
#plt.show()

#-----------------------------------------------------------------------------------------><Matrix plot

flights = sns.load_dataset('flights')
tc= tips.corr()
#sns.heatmap(tc,cmap="coolwarm")
t = flights.pivot_table(index='month',columns='year',values='passengers')
#print(t)
#sns.heatmap(t)
#sns.clustermap(t)
#plt.show()

#-----------------------------------------------------------------------------------------><regression plot

#sns.lmplot(x="total_bill",y="tip",data=tips,hue="sex",markers=['o','v'],col="sex",row="time",aspect=0.6,size=8)
#plt.show()

#-----------------------------------------------------------------------------------------><grid
iris = sns.load_dataset("iris")
#sns.pairplot(iris)
#g= sns.PairGrid(iris)
#g.map(plt.scatter)
#g.map_diag(sns.displot)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)

#----------------facetgrid
#f = sns.FacetGrid(data=tips,col="time",row="smoker")
#f.map(sns.displot,"total_bill")
#or is the plot requires two variable
#f.map(plt.scatter,'total_bill','tip')
#plt.show()

#-----------------------------------------------------------------------------------------><style and colour
#white
#whitegrid
#black
#ticks

#sns.despine()
#plt.figure(figuresize=()) or sns.set_context("",front_scale=)
