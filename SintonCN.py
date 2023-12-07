import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##Gregory Sorghum Yield##
sinton = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\Sinton_CN.csv")
data = sinton[['Yield', '05-24-23NDVI', '06-28-23NDVI']]

x = data['Yield']
y = data['05-24-23NDVI']
z = data['06-28-23NDVI']

#Sinton 05-24-23 NDVI 
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, color='#707070')
plt.plot(x, mymodel)

plt.xlabel('Yield lbs/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')
plt.show()

print(r)
print(p)

#Sinton 06-28-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, z)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, z, color='#707070')
plt.plot(x, mymodel)

plt.xlabel('Yield lbs/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')

plt.show()

print(r)
print(p)
