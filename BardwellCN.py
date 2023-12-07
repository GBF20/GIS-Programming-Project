import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##Bardwell Corn Yield##
bardwell = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\BardwellCN.csv")
data = bardwell[['Yield', '_04-10-23_NDVI', '_05-25-23_NDVI', '_06-14-23_NDVI', '_07-27-23_NDVI']]

x = data['Yield']
y = data['_04-10-23_NDVI']
z = data['_05-25-23_NDVI']
h = data['_06-14-23_NDVI']
n = data['_07-27-23_NDVI']

#Bardwell 04-10-23 NDVI 
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#Bardwell 05-25-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, z)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, z)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#Bardwell 06-14-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, h)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, h)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#Bardwell 07-27-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, n)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, n)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)