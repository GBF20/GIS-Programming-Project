import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##Hondo Corn Yield##
hondo = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\HondoCN.csv")
hondodata = hondo[['Yield', '04-12-23NDVI', '05-19-23NDVI', '07-13-23NDVI']]

x = hondodata['Yield']
y = hondodata['04-12-23NDVI']
n = hondodata['05-19-23NDVI']
z = hondodata['07-13-23NDVI']

#04-12-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))


plt.scatter(x, y, color='#707070')
plt.plot(x, mymodel)
plt.xlabel('Yield bu/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')
plt.show()

print(r)
print(p)

#05-19-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, n)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))


plt.scatter(x, n, color='#707070')
plt.plot(x, mymodel)
plt.xlabel('Yield bu/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')
plt.show()

print(r)
print(p)

#07-13-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, z)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))


plt.scatter(x, z, color='#707070')
plt.plot(x, mymodel)
plt.xlabel('Yield bu/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')
plt.show()

print(r)
print(p)