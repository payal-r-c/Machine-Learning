import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("pollution.csv")
#print (df.head(3))

fig=plt.figure()
ax = fig.add_subplot(1,1,1)
#ax.hist(df['AQI'],bins = 5)
#plt.title('Pollution')
#plt.xlabel('AQI')
#plt.show()

ax.scatter(df['AQI'],df['month'])
plt.xlabel('AQI')
plt.ylabel('Month')
plt.show()
