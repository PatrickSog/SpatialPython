# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:13:31 2019

########################################
# Author: Patrick Sogno
# Date: 28 May, 2019
# Python version: 3.7
# Spyder version: 3.3.2
# e-mail: patrick.sogno@stud-mail.uni-wuerzburg.de
########################################
# Background: 
# This is python homework from university.
# It is therefore mostly for personal use,
# however, if you find something useful for
# your own project, help yourself :).
# I'm a python beginner but I will try to
# answer questions related to the code
# via e-mail.
########################################

@author: patrick
"""





###### Exercise 7: #-------------------------#

import pandas as pd
import numpy as np

path = 'D:\Patrick\Documents\Dokumente\SoSe2019\MET\SpatialPython\climate-change-earth-surface-temperature-data'



# 1. Import ***GlobalLandTemperaturesByCity.csv***

file = 'GlobalLandTemperaturesByCity.csv'


df = pd.read_csv(path + '//' + file)


# 2. Display a summary of the basic information about this DataFrame and its data.

df.head()
df.tail()
df.info()
df.count()
df.index
df.columns
df.values
df.shape



# 3. Select just the 'AverageTemperature' and 'City' columns from the DataFrame df

df.AverageTemperature

df[['AverageTemperature', 'City']]



# 4. Select the 'AverageTemperature' for the years 2000 and 2013

df.where(df['dt'] == '2000').AverageTemperature.head()



# 5. Count the number of cities in the dataset

df['City'].nunique()                # of rows in DataFrame.



# 6. Calculate the mean temperature for each country over all years. Sort the values of 'AverageTemperature' - in decending order

df.head()
df.columns

sortme = df.groupby('Country').mean()
sortme.sort_values('AverageTemperature', ascending = False)



# 7. Calculate the max and min temperature in German cities between 1990 and 2013

dfsub = df.loc[(df['Country'] == 'Germany') & (df['dt'] > '1990-01-01') & (df['dt'] < '2013-12-31')]
dfsub.min()
dfsub.max()



# 8. Calculate the mean temperature change for each city between 1990 and 2013 and sort them in descending order

dfsub = df.loc[(df['dt'] > '1990-01-01') & (df['dt'] < '2013-12-31')]
sortme = dfsub.groupby('City').mean()
sortme.sort_values('AverageTemperature', ascending = False)



# 9. In how many cities can we find increasing temperatures and in how many is the temperature decreasing

df.groupby(['City'])['AverageTemperature'].mean()
first = df.groupby('City')['AverageTemperature'].mean()
last = df.groupby('City')['AverageTemperature'].last()
last
first
diff = last - first
diff
increasing = diff > 0
sum(increasing == True)         # No. of cities with increasing temperatures
sum(increasing == False)        # No. of cities with decreasing temperatures

df.loc[(df['City'] == 'Zwolle')][['AverageTemperature', 'dt']]  # Test with "Zwolle"



# 10. Which city has the highest increase in temperature (which one the highest decrease)

diff.nlargest(1)        # largest increase
diff.nsmallest(1)       # smallest increase



# 11. Is the mean temperatur in German cities increasing or decreasing

dfsub = df.loc[(df['Country'] == 'Germany')]
first = dfsub.groupby('City')['AverageTemperature'].mean()
last = dfsub.groupby('City')['AverageTemperature'].last()
first
last
diff = last - first
diff.cumsum




###### Exercise 8: #-------------------------#

import matplotlib.pyplot

# 1. Calculate the mean temperature of all cities over time and plot the data

clean = df.dropna()
clean
citytemp = clean.groupby('City')['AverageTemperature']
type(citytemp)
citytemp.plot()



# 2. Calculate the mean temperature of Germany over time for spring, summer, autumn, winter.

dfsub = clean.loc[(clean['Country'] == 'Germany')]
dfsub
spring = dfsub[dfsub['dt'].str.contains('-03-' or '-04-' or '-05-')]
spring
summer = dfsub[dfsub['dt'].str.contains('-06-' or '-07-' or '-08-')]
summer
autumn = dfsub[dfsub['dt'].str.contains('-09-' or '-10-' or '-11-')]
autumn
winter = dfsub[dfsub['dt'].str.contains('-12-' or '-01-' or '-02-')]
winter

spring.mean()
summer.mean()
autumn.mean()
winter.mean()

# 3. Calculate the temperature difference between 1900 and 2013 for each german city and plot a ranking based on the temperature difference.

dfsub = clean.loc[(clean['Country'] == 'Germany')]
old = dfsub[dfsub['dt'].str.contains('1900-')]
old = old.groupby('City')['AverageTemperature'].mean()
old

new = dfsub[dfsub['dt'].str.contains('2013-')]
new = new.groupby('City')['AverageTemperature'].mean()
new

diff = new - old
plotme = diff.sort_values(ascending = False)
plotme.plot()
