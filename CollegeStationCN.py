import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##College Station Corn Yield##
cstat = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\College Station CN.csv")
data = cstat[['Yield', '_04-25-23NDVI', '_05-15-23NDVI', '_06-02-23NDVI', '_06-26-23NDVI', '_07-05-23NDVI', '_07-17-23NDVI']]

x = data['Yield']
y = data['_04-25-23NDVI']
z = data['_05-15-23NDVI']
h = data['_06-02-23NDVI']
n = data['_06-26-23NDVI']
m = data['_07-05-23NDVI']
c = data['_07-17-23NDVI']

#College Station 04-25-23 NDVI 
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#College Station 05-15-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, z)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, z)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#College Station 06-02-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, h)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, h)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#College Station 06-26-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, n)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, n)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#College Station 07-05-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, m)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, m)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)

#College Station 07-17-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, c)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, c)
plt.plot(x, mymodel)
plt.show()

print(r)
print(p)