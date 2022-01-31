import matplotlib.pyplot as plt
import pandas as pd

#Reading the CSV file
f =  pd.read_csv("pollution.csv")
#printing the csv file
print (f)
#by using matplotlib print the graph of whole data
f.set_index('year').plot()
plt.show()


f['AQI'].plot(kind='bar', xlabel='AQI')
plt.show()

#Printing the scatter plot
NO = f['NO2μg/l']
years = f['year']

plt.scatter(NO, years, s=100, alpha=0.6, edgecolor='black', linewidth=1)

plt.xlabel('year ')
plt.ylabel('NO2μg/l')

plt.tight_layout()
plt.show()