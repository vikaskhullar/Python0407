# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:09:34 2022

@author: vikas
"""


W = [10, 20, 30, 40]
V = [30, 40, 20, 40]
M = 80
n = 4


knapsackGreProc(W, V, M, n)

def knapsackGreProc(self, W, V, M, n):
    packs = []
    for i in range(n):
        packs.append(KnapsackPackage(W[i], V[i]))
        packs.sort(reverse = True)
        remain = M
        result = 0
        i = 0
        stopProc = False
        while (stopProc != True):
             if (packs[i].weight <= remain):
                 remain -= packs[i].weight;
                 result += packs[i].value;
        print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)
        if (packs[i].weight > remain):
            i += 1
            if (i == n):
                stopProc = True
        print("Max Value:t", result)