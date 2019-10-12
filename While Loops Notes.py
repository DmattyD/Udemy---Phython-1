#!/usr/bin/env python
# coding: utf-8

# While Loop Notes

#     While loops will continue to execute a block of code WHILE some condtions remain true.
#     
#     For example, WHILE my pool is not full, keep adding water.
#     
#     Or, WHILE the dogs are hungry, keep feeding them.

# SYNTAX:
#     
#     while some_boolean_condition:
#     
#         do somthing
#         
#     else:
#     
#         do something different

# In[3]:


x = 0

while x <= 5:
    print(f'The current value of x is {x}')
    x = x+1
    #x += 1


# In[5]:


x = 0
while x < 5:
    print(f'The current value of x is {x}')
    
    x += 1
else:
    print('X IS NOT LESS THAN 5')


# Break // Continue // Pass
# 
# these statements add additional funcational for various cases.
# 
# break: breaks out of the current closest enclosing loop.
# 
# continue: goes to the top of the closest enclosing loop.
# 
# pass: does nothing at all - (This is also a placeholder to avoid an error)

# In[6]:


x = [1,2,3]


# In[7]:


for item in x:
    pass


# Continue:

# In[8]:


mystring = 'Sammy'


# In[10]:


for letter in mystring:
    if letter == 'a':
        continue
    print(letter)


# Break:

# In[13]:


for letter in mystring:
    if letter == 'm':
        break
    print(letter)


# In[14]:


x = 0

while x < 5:
    
    if x == 2:
        break
    print(x)
    x += 1


# In[ ]:




