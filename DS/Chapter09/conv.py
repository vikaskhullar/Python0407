# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 19:49:50 2022

@author: vikas
"""

f = open('aa.txt','r')
a =f.readline()
col = a.replace('\n','').split(',')[1:]
col
row=[]
graph = dict()  
a=f.readline()

col

while(a):
    b = a.replace('\n','').split(',')
    c= b[0]
    row=[]
    for i in range(1,len(b[1:])+1):
        if(b[i]=='1'):
            row.append(col[i-1])
    
    graph[c]= row
    a=f.readline()
    
graph


