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
# uniform number 
u1 = np.random.uniform(1,0,1000000)
u2 = np.random.uniform(1,0,1000000)
# sns.distplot(u1)
# sns.distplot(u2)
#Gaussian number genration with 0 mean and variance 1
r = np.sqrt(-2*np.log(u1))
U1 = r*np.cos(2*3.141*u2)
U2 = r*np.sin(2*3.141*u2)
#Rayleigh distribution
rayleigh = np.sqrt(U1**2 + U2**2)
#Exponential Distribution
exp = rayleigh**2 
sns.distplot(exp)
plt.figure()
sns.ecdfplot(exp) 
print(np.var(exp))
print(np.mean(exp))
