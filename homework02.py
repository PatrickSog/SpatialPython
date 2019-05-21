########################################
# Author: Patrick Sogno
# Date: 21 May, 2019
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







###### Exercise 6: #-------------------------#
# 1. Create null vector of size 10
import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a)
a.shape

# 2. Sort random vector of size 10
a = np.random.rand(10)
print(a)
a.sort()
print(a)

# 3. Create 3x3 matrix with values 0 to 8
a = np.array([[0,1,2], [3,4,5], [6,7,8]])
print(a)

# 4. 2d array with 1 on border and 0 inside
l = int(input("Length of the frame: "))
h = int(input("Height of the frame: "))

x = np.ones((h,l))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)
# -----------> Solution found here: 
# https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-8.php

# 5. 8x8 matrix with checkerboard pattern
x = np.zeros((8,8))
print(x)
x[1::2, ::2] = 1
print(x)
x[0::2, 1::2] = 1
print(x)
# -----------> Solution found here: 
# https://www.geeksforgeeks.org/python-program-print-checkerboard-pattern-nxn-using-numpy/

# 6. Create random array and subtract mean of each row of a matrix (array?)
h = np.random.randint(1,10) # random height of the array
print(h)
l = np.random.randint(1,10) # random length of the array
print(l)

a = np.random.rand(h,l) # produce random array
print(a)
m = np.array(np.mean(a, axis = 0)) # mean of each row
print(m)
np.subtract(a, m) # subtract mean from array

# 7. Random 10x2 matrix representing cartesian coordinates, convert to polar coordinates
a = np.random.rand(10,2)
print(a)

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

cart2pol(a[0::1, 0], a[0::1, 1])
# -----------> Solution found here: 
# https://stackoverflow.com/questions/20924085/python-conversion-between-coordinates

# 8. Random vector with shape (100,2) representing coordinates, find point to point distances
a = np.random.rand(100,2)
print(a)
print(a[0,0])
print(a[0,1])
from math import sqrt

d = []
for i in range(99):
    distance = [sqrt( ((a[i,0]-a[i+1,0])**2)+((a[i,1]-a[i+1,1])**2) )]
    d.extend(distance)
print(d)

###### End of script. #-------------------------#
