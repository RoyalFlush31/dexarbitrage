#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:11:01 2020

@author: lennert
"""

import timeit
import numpy as np
from AfterPoolValues import AfterPoolValues

start = timeit.timeit()

a = ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 900000, "DAI:", 10000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 11000000], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 10700000], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 10000000], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 9600000], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 8900000], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "ETH:", 1000000, "DAI:", 8700000]    
C2 = ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 10026000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 10000000, "BAT:", 11080000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 11111111], ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 11119000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 11107000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 11120000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "DAI:", 9000000, "BAT:", 11100000]
C3 = ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 1300000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 1010000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 830000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 950000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 800000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 1010000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "BAT:", 10000000, "SNX:", 1100000000]
C4 = ["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1005000000, "ETH:", 1000000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 900000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 805045],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 980000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 720000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 970000],["0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", "SNX:", 1000000000, "ETH:", 930000]
token1 = "ETH:"
token2 = "DAI:"


def mean_max(pool):
    z = np.array(pool)
    x = 0
    mean = 0
    max_value = 0
    for j in range(len(z)):
        token1 = z[j, 1]
        token2 = z[j, 3]
    for x in range(len(z)):                   
        if z[x,1] == token1 and z[x,3] == token2 :  
            preis =  float(z[x,4]) / float(z[x,2])       
            mean = mean + preis
            if preis > max_value:
                    max_value = preis
                    adresse = (z[x,0:])
                    limit = 0.15 * float(z[x,2])
            min_value = preis
            if preis < min_value:
                    min_value = preis
                    adresse = (z[x,0:])
                    limit2 = 0.15 * float(z[x,2])
    x = + 1
    mean = mean / len(z)
    if limit <= limit2:
        limit = limit2
    adresse = np.append(adresse,max_value)
    adresse = np.append(adresse,min_value)
    adresse = np.append(adresse,mean)
    adresse = np.append(adresse, int(limit))
    return adresse

def perfectEntryAmount(C):
    a = AfterPoolValues(mean_max(C))
    return a
    
    
    
print(mean_max(C2))
#print(AfterPoolValues(mean_max(C3,"BAT:","SNX:")))
#print(mean_max(C4,"SNX:","ETH:"))



#end = timeit.timeit()
#print(end - start)    









