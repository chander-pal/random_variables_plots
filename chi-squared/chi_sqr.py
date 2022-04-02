#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 02:42:18 2021

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
u3 = np.random.uniform(1,0,1000000)
u4 = np.random.uniform(1,0,1000000)
# sns.distplot(u1)
# sns.distplot(u2)
#Gaussian number genration with 0 mean and variance 1
r1 = np.sqrt(-2*np.log(u1))
G1 = r1*np.cos(2*3.141*u2)
G2 = r1*np.sin(2*3.141*u2)
r2 = np.sqrt(-2*np.log(u3))
G3 = r2*np.cos(2*3.141*u4)
G4 = r2*np.sin(2*3.141*u4)
#replace to desired value
var_g = np.sqrt(1);
mean_g = 2;
U1 = var_g*G1+mean_g
U2 = var_g*G2+mean_g
U3 = var_g*G3+mean_g
U4 = var_g*G4+mean_g
#chi_square defination
ch_sq = (U1**2 + U2**2+U3**2 + U4**2)
sns.distplot(ch_sq)
plt.figure()
#cdf plot
sns.ecdfplot(ch_sq) 
print(np.var(ch_sq))
print(np.mean(ch_sq))
