#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:00:05 2021

@author: chanderpal
"""
import numpy as np
def uniform_number(up,low,mult,lin,mod,seed,size):
    U = np.zeros(size)
    Un = np.zeros(size)
    x = (seed*mult + lin)%mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult+lin)%mod
        U[i] = x/mod
        Un[i] = low +(up-low)*U[i]
    return Un