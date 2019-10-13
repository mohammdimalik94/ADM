#!/usr/bin/env python
# coding: utf-8

# # Python

# Say "Hello, World!" With Python



print("Hello, World!")


# Python If-Else

n = 24
if(n % 2 !=0):
    print("Weird")
elif((n % 2 == 0) and (5 <= n >= 2)):
    print("Not Weird")
elif((n % 2 == 0) and (20 <= n >= 6)):
    print("Weird")
elif((n % 2 == 0) and (n > 20)):
    print("not Weird")
        


# Arithmetic Operators
# 
# 

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    summ = a + b
    sub = a - b
    mult = a * b
    print(summ)
    print(sub)
    print(mult)


# Python: Division
#


x = int(input())
y = int(input())
print(x//y)
print(x/y)


# Loops



x = int(input())
for i in range(x):
    print(i**2)


# Write a function
# 
# 

# In[ ]:


def is_leap(y):
    if (y % 4 == 0):
        leap = False
        if(y % 100 == 0) and (y % 400 != 0):
            return False
        else:
            return True
    else:
        return False
        
year = int(input())


# Print Function
# 
# 

# In[ ]:


n = int(input()) 
for i in range(1 ,n+1):
    print(i,end='')


# # BASIC DATA TYPES

# List Comprehensions
# 
# 

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j+ k != n ] 
    print(x)


# Find the Runner-Up Score!



n  = input()
score = sorted(set(map(int , input().split())))
print(score[-2])


# Lists

# In[ ]:


list = []
n = int(input())
for i in range(0,n):
    s = input().split(" ")
    command_type = s[0]
    i = 1
    while i < len(s):
        s[i] = int(s[i])
        i += 1
    if command_type == "append":
        list.append(s[1])
    elif command_type == "insert":
        list.insert(s[1],s[2])
    elif command_type == "remove":
        list.remove(s[1])
    elif command_type == "pop":
        list.pop()
    elif command_type == "index":
        list.index(s[1])
    elif command_type =="count":
        list.count()
    elif command_type =="sort":
        list.sort()
    elif command_type == "reverse":
        list.reverse()
    elif command_type == "print":
        print(list)


# Tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())


# 

# # STRING
# 

# sWAP cASE
# 
# 

# In[ ]:


def swap_case(s):
    x = s.swapcase()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join
# 
# 

# In[ ]:


x = "this is a string"
x = x.split('-')
print(x)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?
# 
# 

# In[ ]:


def print_full_name(a, b):
    print("")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations
# 
# 

# In[ ]:


def mutate_string(string,postion,char):
    string = list(string)
    string[postion] = char
    return "".join(string)    


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string
# 
# 

# In[ ]:


def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if string[i : i+sub_len] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# String Validators
# 
# 

# In[ ]:


s = input()
print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))


# Text Wrap
# 
# 

# In[ ]:


import textwrap

def wrap(string, max_width):
    string_wrap = textwrap.fill(string,max_width) 
    return string_wrap

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Capitalize

# In[ ]:


import math
import os
import random
import re
import sys

def solve(s):
        return " ".join([n.capitalize() for n in name.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Collections
# 

# collections.Counter()

# In[ ]:


from collections import Counter
X = int(input())
sizes = Counter(map(int, input().split()))
earn = 0
for i in range(int(input())):
    size, price = map(int, input().split())
    if size in sizes.keys() and sizes.get(size)>0:
        earn += price
        sizes[size] -= 1    
print(earn)


# Collections.namedtuple()
# 
# 

# In[ ]:


from collections import namedtuple
N, categories = int(input()), input().upper().split()
student_sheet_fill = namedtuple("student_sheet_fill",categories)
count_marks = 0
for i in range(N):
    a,b,c,d = input().split()
    student_sheet = student_sheet_fill(a,b,c,d)
    count_marks += int(student_sheet.MARKS)
print(count_marks/N)


# Collections.deque()

# In[ ]:


from collections import deque
d=deque()
N=int(input())
for i in range(N):
    n=(input().split())    
    if n[0]=="append":
        d.append(n[1])
    elif n[0]=="appendleft":
        d.appendleft(n[1])
    elif n[0]=="pop":
        d.pop()
    elif n[0]=="popleft":
        d.popleft()
for i in d:
    print(i,end=" ")


# # itertools

# itertools.product()

# In[ ]:


from itertools import product
A = map(int,input().split())
B = map(int, input().split())
print(*product(A,B))


# itertools.permutations()

# from itertools import permutations
# s, k = input().split()
# permutations = list(permutations(s, int(k)))
# permutations.sort()
# for i in permutations:
#     print("".join(i))

# itertools.combinations()
# 
# 

# In[ ]:


from itertools import combinations
s = input().upper().split()
string, value = sorted(s[0]), int(s[1])
for i in range(1, value + 1):
    print(*list(map(''.join, combinations(string, i))), sep='\n')


# itertools.combinations_with_replacement()

# In[ ]:


from itertools import combinations_with_replacement
s = input().upper().split()
string, value = sorted(s[0]), int(s[1])
print(*list(map(''.join, combinations_with_replacement(string, value))), sep='\n')


# # sets
# 

# Introduction to Sets
# 
# 

# In[ ]:


def average(array):
    arr =set(array)
    sum_arr = sum(arr)
    len_arr = len(arr)
    x= sum_arr/len_arr
    return x
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# Set .add()

# In[ ]:


n = int(input())
s = set()
for i in range(n):
    s.add(input())
print(len(s))


# Set .union() Operation
# 
# 

# In[ ]:


set1_size = int(input())
set1 = set(map(int,input().split()))
set2_size = int(input())
set2 = set(map(int,input().split()))
print(len(set1.union(set2)))


# Set .discard(), .remove() & .pop()
# 
# 

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    string = input().split()
    if string[0] == 'pop': s.pop()
    elif string[0] == 'remove': s.remove(int(string[1]))
    elif string[0] == 'discard': s.discard(int(string[1]))
print(sum(s))


# Set .intersection() Operation
# 
# 

# In[ ]:


set1_size = int(input())
set1 = set(map(int,input().split()))
set2_size = int(input())
set2 = set(map(int,input().split()))
print(len(set1.intersection(set2)))


# Set .difference() Operation
# 
# 

# In[ ]:


a,lista=(int(input()),input().split())
seta=set(lista)
c,listb=(int(input()),input().split())
setb=set(listb)
result = seta.difference(setb)
print(len(result))


# Symmetric Difference
# 
# 

# set1=input()
# a = set(input().split())
# input()
# b = set(input().split())
# union = a.union(b)
# intersection = a.intersection(b)
# symatric = union.difference(intersection)
# for i in symatric:
#     print(i,i+1)

# Set Mutations
# 
# 

# In[ ]:


size1 = int(input())
s1 = set(map(int, input().split()))
n = int(input())

for i in range(n):
    s, size2 = input().split()
    s2 = set(map(int, input().split()))
    if(s == "intersection_update"):
        s1.intersection_update(s2)
    elif(s == "update"):
        s1.update(s2)
    elif(s == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(s == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))


# Check Subset
# 
# 

# In[ ]:


for i in range(int(input())):
    A, seta = input(), set(input().split())
    B, setb = input(), set(input().split())
    print(all([i in setb for i in seta]))


# # DATE and TIME

# Calendar Module
# 
# 

# In[ ]:


import datetime   
def findDay(day,month, year):      
    born = datetime.date(year, day, month) 
    return born.strftime("%A") 
day, month, year = map(int ,input().split())
d = findDay(day,month, year)
print(d.upper())


# In[ ]:




