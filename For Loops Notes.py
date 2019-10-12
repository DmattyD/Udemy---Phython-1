#!/usr/bin/env python
# coding: utf-8

# For Loops Notes

# For loops are used to execute a block of code for every iteration.

# Iterate over every character in a string, or every key in a dictionary, or item in a list

# SYNTAX:
#     my_iterable = [1,2,3]
#     for item_name in my_iterable:
#         print(item_name)
# >> 1
# 
# >> 2
# 
# >> 3

# the assignment can have any assigned value

# In[1]:


my_iterable = [1,2,3]


# In[2]:


for item_name in my_iterable:
    print(item_name)


# In[3]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[5]:


for x in mylist:
    print(x)


# The for loop does not have to return the values or the assignment, it can return a string or another value, as shown below

# In[6]:


for x in mylist:
    print('This is a number!!!')


# logical operators and control flow can also be utilized in for loops

# In[8]:


for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)


# In[10]:


for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print('I"m an odd number!')


# f-string literals can also be utilized

# In[12]:


for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')


# Keep a tally during running loops.  In the example below, due to whitespace, it will only return the total value.

# In[19]:


for num in mylist:
    list_sum = list_sum + num
print(list_sum)


# to create a running tally, make sure to include the print('x') without the whitespace.

# In[15]:


list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)


# In[18]:


list_sum = 0


# In[20]:


for x in 'Hello World':
    print(x)


# a _ can be used if the desired outcome is to print something like below, and not assign a variable to the outcome

# In[21]:


for _ in 'Hello World':
    print('Cool!')


# Tuple unpacking via for loops

# In[23]:


tup = (1,2,3)

for item in tup:
    print(item)


# In[24]:


tuple_list = [(1,2),(3,4),(5,6),(7,8)]


# In[25]:


len(tuple_list)


# In[26]:


for item in tuple_list:
    print(item)


# Tuple Unpacking
# 
# Unpacking is where a variable is created, as (a,b) below, that mimics a tuple.  Then that item is called in the for loop, and it will return the values within the tuple as called

# In[29]:


for (a,b) in tuple_list:
    print(a)
    print(b)


# In[30]:


for a,b in tuple_list:
    print(b)


# In[31]:


new_list = [(1,2,3),(4,5,6),(7,8,9)]


# In[32]:


for n in new_list:
    print(n)


# In[33]:


for a,b,c in new_list:
    print(b)


# Iterating Through a Dictionary
# 
# by default, when iterating through a dictionary, it will iterate through the keys, NOT the values

# In[34]:


d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)


# to iterate through the items of a dictionary, (keys and values), .items() method needs to be used

# In[35]:


for item in d.items():
    print(item)


# To get the values, as opposed to the keys, tuple unpacking is needed

# In[37]:


for k,v in d.items():
    print(v)


# In[ ]:




