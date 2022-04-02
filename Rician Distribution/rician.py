#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 23:04:52 2021

@author: chanderpal
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#uniform numbers
u1 = np.random.uniform(1,0,1000000)
u2 = np.random.uniform(1,0,1000000)
# sns.distplot(u1)
# sns.distplot(u2)
#Gaussian number genration with 0 mean and variance 1
r = np.sqrt(-2*np.log(u1))
G1 = r*np.cos(2*3.141*u2)
G2 = r*np.sin(2*3.141*u2)
#replace to desired value
var_g = np.sqrt(25);
mean_g = 1;
U1 = var_g*G1+mean_g
U2 = var_g*G2+mean_g
print("Mean and Variance of Gaussian variable U1 is")
print(np.mean(U1),np.var(U1))
print("Mean and Variance of Gaussian variable U2 is" )
print(np.mean(U2),np.var(U2))
#rician pdf
rician = np.sqrt(U1**2 + U2**2)
sns.distplot(rician)
plt.figure()
#cdf plot
# sns.ecdfplot(rician) 
print(np.var(rician))
print(np.mean(rician))
