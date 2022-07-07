# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 18:59:33 2022

@author: vikas
"""

x = iter(["apple", "banana", "cherry"])
x

print(next(x))
print(next(x))
print(next(x))
print(next(x)) #StopIteration


len(a)

max(iter(["apple", "banana", "cherry"]))

x=iter([1,4,2])

a = sum(x)
a

type(x)

abs(-11.7)

mylist = [True, True, False]

len(mylist)



#Control Statements

a= 10
b= 20
c= 30

if (a<b):
    print("A is lesser")



if (a>b):
    print("A is lesser")



if (a<b):
    print("A is lesser")
else:
    print("B is lesser")




if (a>b):
    print("A is lesser")
else:
    print("B is lesser")



marks = int(input("Enter Marks-> "))

if (marks>90):
    print("A")
elif (marks>80 and marks<=90):
    print("B")
elif(marks>70 and marks<=80):
    print("C")
elif(marks>60 and marks<=70):
    print("D")
else:
    print("Fail")





switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";




#Month and Year Query

month = int(input("Enter Month->"))
year = int(input("Enter Year->"))


days=0
if(month== 1):
    days= 31
elif(month== 2):
    if (year%4==0):
        days= 29
    else:
        days=28
elif(month== 3):
    days= 31
elif(month== 4):
    days= 30
elif(month== 5):
    days= 31
elif(month== 6):
    days= 30
elif(month== 7):
    days= 31
elif(month== 8):
    days= 31
elif(month== 9):
    days= 30
elif(month== 10):
    days= 31
elif(month== 11):
    days= 30
elif(month== 12):
    days= 31
else:
    print("Enter Valid Month")    

print(f"No of days in Month {month} of Year {year} is {days}")



#Looping


l1 = [2,5,4,7,8,9]

for i in l1:
    print(i)


j=2
for i in range(1,11):
    print(f"{j} * {i} = {j*i}")



#Nested Loops

for j in range(2,5):
    for i in range(1,11):
        print(f"{j} * {i} = {j*i}")
print("Completed")


for i in range(1,6):
    for j in range(1,i+1):
        print("*", end='')
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(i, end='')
    print()




a = list(range(1,6))
a.reverse()
a


for i in a:
    for j in range(1,i+1):
        print('*', end='')
    print()



for i in a:
    for j in range(1,i+1):
        print('*', end='')
    print()




for i in range(1,6):
    for k in range(1,6-i):
        print(' ',end='' )
    for j in range(1,i+1):
        print(j, end='')
    
    a = list(range(1,i))
    a.reverse()
    for l in a:
        print(l,end='')
    
    print()


# While

while(False):
    print("Hello")


while(True):
    print("Hello")

# Conditional Check statements apply

i = 1

while(i<=10):
    print(i)
    i=i+1
    


i=1
while(i<=5):
    j=1
    while(j<=i):
        print(j,end='')
        j=j+1
    i=i+1
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()



































































































