#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 23:00:22 2021

@author: chanderpal
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#uniform random numbers
u1 = np.random.uniform(1,0,1000000)
u2 = np.random.uniform(1,0,1000000)
# sns.distplot(u1)
# sns.distplot(u2)
#Gaussian number genration with 0 mean and variance 1
r = np.sqrt(-2*np.log(u1))
U1 = r*np.cos(2*3.141*u2)
U2 = r*np.sin(2*3.141*u2)
#Rayleigh random numbers
rayleigh = np.sqrt(U1**2 + U2**2)
sns.distplot(rayleigh)
plt.figure()
sns.ecdfplot(rayleigh) 
print(np.var(rayleigh))
print(np.mean(rayleigh))
