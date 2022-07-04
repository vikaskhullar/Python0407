# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:04:24 2022

@author: vikas
"""

print()

#inputs or parameters

print?

print("Hi")

print("Hi", "Welcome", "To", "Python")

print("Hi", "Welcome", "To", "Python", sep="-")


print("Hi")
print("Welcome")
print("To", "Python")

print?


# Special Cobination of strings
#'\n' , '\t', '\b'


print("Hi Welcome \n to Python")


print(r"Hi Welcome \n to Python")

print("Hi", end='-')
print("Welcome")
print("To", "Python")


country = "India"

country

print("I live in India")

print("I live in country")

print("I live in", country)

print("I live in", country, sep='-')

print(f"I live in {country}")

country


lcountry = input("Enter Country Name->")
wcountry = input("Enter Work Country")

print(f"I live in {lcountry} and work in {wcountry}")


a = 10
b = 20
c = a+b


a = input("Enter A->")

c = a+b #TypeError: can only concatenate str (not "int") to str


b = input("Enter B->")

c = a + b


#Type casting or type conversion

a = int(input("Enter A->"))
b = int(input("Enter B->"))

c = a+b

r = "Value of C is " + str(c)
r

print(r)

# Demonstrate int() Casting Function

float_to_int = int(3.5)
string_to_int = int("1")
print(f"After Float to Integer Casting the result is {float_to_int}")
print(f"After String to Integer Casting the result is {string_to_int}")


# Demonstrate float() Casting Function

int_to_float = float(4)
string_to_float = float("1")
print(f"After Integer to Float Casting the result is {int_to_float}")
print(f"After String to Float Casting the result is {string_to_float}")

# Demonstrate str() Casting Function

int_to_string = str(8)
float_to_string = str(3.5)
print(f"After Integer to String Casting the result is {float_to_string}")
print(f"After Float to String Casting the result is {float_to_string}")


ch = 'a'
ord(ch)

ch = 'Z'
ord(ch)

ch = '!'
ord(ch)

asc = 99
chr(asc)

asc = 60
chr(asc)


ch = input("Enter a Char-> ")
if (ord(ch)>=65 and ord(ch)<=90):
    print("Entered Alphabet")
else:
    print("Not Entered Alphabet")


#Airthmatic Operations

x = 10

print(x)
print(x+10)
print(x-10)
print(x/10)
print(x*10)

print(x**4)
print(x%3)


num = int(input("Enter a Number->"))

if (num%2 == 0):
    print("Even Number")
else:
    print("Odd Number")


print(x)

x = x * 2
x

y = x * 2
y

#Comparative Operators

a = 10
b = 20

a == b
a<b
a<=b
a>b
a>=b
a!=b

# Boolean

t = True
f = False

f and f
f and t
t and f
t and t

f or f
f or t
t or f
t or t



a = 10
b = 20
c = 30


a<b
b<c


a<b and b<c
a<b and b>c



a<b or b<c
a<b or b>c
a>b or b>c


if(a<b and b<c):
    print("C is Greater")


not t
not f


# List, Set, Dictionary, Tuple

l1 = []

l1 = [10,20,30,40,50,60]

print(l1)

#Indexed

l1[0]
l1[2]
l1[5]
l1[6] #IndexError: list index out of range


r1 = range(10)
r1
l2 = list(r1)
l2

r2 = range(10, 20)
r2
l3 = list(r2)
l3

r3 = range(10, 101, 5)
r3
l4 = list(r3)
l4

'''
Dont Use this code. this will consume maximum available memory
r4 = range(100000001)
l5 = list(r4)
len(l5)
l5[100000000]
'''


#Dont Use this code. this will consume maximum available memory

l1 = list(range(10, 101, 5))
l1

#Indexed

l1[0]
l1[1]
l1[2]

for i in l1:
    print(i)



for i in l1:
    print(i)
print("Out")

#Mutable or Changable

l1[5]=108
l1

#Hetrogeneous

l2 = [10, 44.6, 'VK', True]
l2


for i in l2:
    print(type(i))


#Unordered
l4 = [3,7,4,9,8,1,2]

l4[0:3]
l4[:3]
l4[3:]
l4[-1]
l4[-2:]
l4[-4:-2]


l4
l4.pop()
l4

l4.pop(2)
l4.pop(4)

l4

l4.append(10)
l4

l4.append(67)
l4

l4.insert(2, 44)
l4


l4.clear()

del l4


#Set

# No Duplicates, Always in order

s1 = {7,5,3,9,1}

# Ordered
s1

s2 = {3,4,8,6,1,4,3,2,7,8}

#No Duplicate Values
s2

#Not Indexed
s2[2] #TypeError: 'set' object is not subscriptable

for i in s2:
    print(i)


for i in s2:
    print(i*2)


#Hetrogeneous

s3 = {10, 22.2, "SK", True}
s3


s3.add(100)
s3

s2.add(10)
s2

s2.pop()
s2.remove(4)
s2
s2.remove(4) #KeyError: 4
s2
s2.discard(6)
s2
s2.discard(6)
s2

s4 = {2,4,3,6}
s5 = {5,3,4,2}

s4.union(s5)
s4.intersection(s5)
s4.difference(s5)



#tuple

#Non Mutable

t1 = (10,4,3,6,11)

t1

#Indexed
t1[0]

t1[2]

t1[2]=3 #TypeError: 'tuple' object does not support item assignment


t1.add() #TypeError: 'tuple' object does not support item assignment


#Hetrogeneous Data


t2 = ['aa', 10, 10.4, True]
t2


# find number of days in a month
#leap year

year%4 ==0 

feb=29

































































































































