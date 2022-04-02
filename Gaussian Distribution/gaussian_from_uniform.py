#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:46:01 2021

@author: chanderpal
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')
# uniform number 
u1 = np.random.uniform(1,0,1000000)
u2 = np.random.uniform(1,0,1000000)
# sns.distplot(u1)
# sns.distplot(u2)
#Gaussian number genration with 0 mean and variance 1
r = np.sqrt(-2*np.log(u1))
G1 = r*np.cos(2*3.141*u2)
G2 = r*np.sin(2*3.141*u2)
# replace to desired value
var_g = np.sqrt(1);
mean_g = 0;
U1 = var_g*G1+mean_g
U2 = var_g*G2+mean_g
plt.figure()
sns.set_style('darkgrid')
sns.distplot(U1) #1st pdf
plt.figure()
sns.distplot(U2) #2nd pdf
plt.figure()
sns.set_style('darkgrid')
sns.distplot(U1) #Combine or overlaping pdf of U1 and U2
sns.distplot(U2)
print(np.var(U1))
print(np.var(U2))
print(np.mean(U1))
print(np.mean(U2))
