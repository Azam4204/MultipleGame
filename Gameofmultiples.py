#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:56:09 2021

@author: azam
"""

t=int(input())
total=[]
for i in range(t): 
    n=int(input())
    sum=0
    for j in range(n):
        if j%3==0 or j%5==0:
            sum+=j
    total.append(sum)
k=0
while(k<len(total)):
    print(total[k])
    k+=1