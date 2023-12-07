import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##Rosenberg Sorghum Yield##
rosen = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\RosenbergGS.csv")
data = rosen[['Yield', '04-03-23NDVI', '05-22-23NDVI', '07-06-23NDVI', '040323mNDVI']]

x = data['Yield']
y = data['04-03-23NDVI']
m = data['05-22-23NDVI']
h = data['07-06-23NDVI']

#Rosenberg 04-03-23NDVI 
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#Rosenberg 05-22-23NDVI
slope, intercept, r, p, std_err = stats.linregress(x, m)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, m)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#Rosenberg 07-06-23NDVI
slope, intercept, r, p, std_err = stats.linregress(x, h)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, h)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)
