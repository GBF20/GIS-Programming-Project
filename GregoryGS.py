import sys
import matplotlib.pyplot as plt

import pandas as pd
from scipy import stats

##Gregory Sorghum Yield##
gregory = pd.read_csv(r"C:\Users\Bruno\OneDrive - Texas A&M AgriLife\Desktop\GIS Programming\Project\Yield Data\Harvest_Joins\GregoryGS.csv")
data = gregory[['Yield', '03-24-23NDVI', '05-24-23NDVI', '06-28-23NDVI']]

x = data['Yield']
y = data['03-24-23NDVI']
z = data['05-24-23NDVI']
h = data['06-28-23NDVI']

#Gregory 03-24-23 NDVI 
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

#Gregory 05-24-23 NDVI
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

#Gregory 06-28-23 NDVI
slope, intercept, r, p, std_err = stats.linregress(x, h)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, h, color='#707070')
plt.plot(x, mymodel)

plt.xlabel('Yield lbs/acre')
plt.ylabel('NDVI')
plt.title('NDVI vs. Yield')

plt.show()

print(r)
print(p)
