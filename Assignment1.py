#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python program to get the Fibonacci series between 0 to 50
a,b=0,1
while b<50:
    print(b)
    a,b = b,a+b


# In[4]:


#Write a Python program that accepts a word from the user and reverse it.
x = input("Enter your name: ")
for i in range(len(x) -1,-1,-1):
    print(x[i], end="")
print("\n")


# In[9]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
odd=0
even=0
for i in numbers:
        if not i % 2:
             even+=1
        else:
             odd+=1
print("Even numbers are:",even)
print("Odd numbers are:",odd)


# In[ ]:




