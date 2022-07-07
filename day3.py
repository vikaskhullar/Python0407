# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:02:49 2022

@author: vikas
"""

l1 = ["eat", "sleep", "repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
    
    
    
x = (['apple', 'banana', 'cherry'],["eat", "sleep", "repeat"])

y = enumerate(x)

y

for i in y:
    print(i)



def factorial(n):
    if (n==1 or n==0):
        print(n)
        return(1)
    else:
        print(f"{n} * factorial({n - 1})")
        return(n * factorial(n - 1))
        
num = 5;
print("Factorial of",num,"is",
factorial(num))






def Fibonacci(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))


'''
Given a number x, determine whether the given number is Armstrong number or not. 
A positive integer of n digits is called an Armstrong number of order n 
(order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

'''

num = int(input("Enter a number: "))

sum = 0

temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** len(str(num))
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
   
   
   
   
num = 24
flag = False

if num > 1:
    for i in range(2, int(num/2)):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
    
    

#Write a Python program to get the difference between the two lists.

l1 = [3,4,5,6]
l2 = [4,5,7,8]

s1= set(l1)
s2 = set(l2)


s3 = s1.intersection(s2)
s3
s4 = s1.union(s2)
s4
s5 = s4.difference(s3)
s5


l3 = []
for i in l1:
    if (i not in l2):
        l3.append(i)
for i in l2:
    if (i not in l1):
        l3.append(i)
        

print(l3)


#Write a Python program to find the second smallest number in a list.

l1 = [7,8,3,4,5,6]
l1.sort()
l1[-2]


m = 0
for i in l1:
    if(i > m):
        m=i

a=0
for i in l1:
    if (i>a and i !=m):
        a=i
print(a)











































    