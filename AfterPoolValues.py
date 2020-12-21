#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:49:31 2020

@author: lennert
"""

C1 = [0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2, "ETH:", 900000, "DAI:", 10000000, 11.1111, 10, 100000]
C2 = [0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2, "DAI:", 9000000, "BAT:", 10026000, 1.114, 1.111, 1000000]


def AfterPoolValues(C):
    list1 = []
    list2 = []
    list3 = []
    m = float(C[6])
    PoETH = float(C[2])
    PoDAI = float(C[4])
    h = int(C[7])
    
    for i in range(h):
        i = i + 1
        newRatio  = (PoDAI-((i/PoETH)*PoDAI)) / (PoETH + i)
        a = newRatio 
        if a >= 0:
            list1.append(a)
            list2.append(i)
    for i in range(len(list1)):
        g = list1[i]
        if g >= m:
            list3.append(g)
            

    perfectPoolBalance = min(list3)
    perfectFlashloan = list2[list1.index(perfectPoolBalance)]
    
    return perfectPoolBalance, perfectFlashloan
   






















