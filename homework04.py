# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:35:28 2019

########################################
# Author: Patrick Sogno
# Date: 04 June, 2019
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

###### Preparation: #-------------------------#

# set paths

filepath = "D:/Patrick/Documents/Dokumente/SoSe2019/MET/SpatialPython/SpatialPython2019-master/Data/NPBF"
baumdaten = "Baumdaten.xlsx"
position = "Position.xlsx"
verjuengung = "Verjuengung und Bodenvegetation.xlsx"

# import

import geopandas as gpd
import pandas as pd



###### Exercise 1: #-------------------------#

# 1. Import Baumdaten.xlsx and Position.xlsx

baumfile = pd.read_excel(filepath + "//" + baumdaten)
positionfile = pd.read_excel(filepath + "//" + position)



# 2. Create a spatial point data set with the position of each tree (CRS: DHDN / 3-degree Gauss zone 4)

baumfile
type(baumfile)
list(baumfile)
positionfile
list(positionfile)

bp = baumfile.merge(positionfile, on='Koord')
list(bp)
type(bp)
df = pd.DataFrame(bp)
type(df)
df.GK_X = df.GK_X.astype('float64')
df.GK_Y = df.GK_Y.astype('float64')
df.dtypes

gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.GK_X, df.GK_Y))
gdf.crs = {'init': '31468'}
gdf.head()



# 3. Create a map which shows,
#    - each tree postion
#    - tree species
#    - height
#    - DBH

gdf.plot()  # position
list(gdf)
gdf.plot('Hoehe')   # height
gdf.plot('Baumart') # species
gdf.plot('BHD') # diameter



###### End of script. #-------------------------#

