# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:14:03 2022

@author: vikas
"""

W = [10, 20, 30, 40]
V = [30, 40, 20, 40]
M = 80
n = 4
F = [0] *n
F

import pandas as pd
df = pd.DataFrame({'W':W, 'V':V})
df['F'] = df['V']/df['W']

df

df = df.sort_values(by='F', ascending=False)
df

dt = df.values.T

dt

W = dt[0]
V = dt[1]
F =dt[2]


print(W)
print(V)
print(F)

FW=0
FV=0
flg=0

for i in range(0,n):
    if (FW==M):
        break
    else:
        FW=FW+W[i]
        FV=FV+V[i]
        if(FW>M):
            FW= FW - W[i]
            FV= FV - V[i]
            PW = M-FW
            FV = FV + F[i]*PW
            break
print(f"Final Weight i {FW} and Final Value is {FV}")




























