#!/usr/bin/env python
# coding: utf-8

# Formatting with the .format() method
# 
# A good way to format objects into strings is with the string.format() method.
# 
# SYNTAX: 'String here {}'.format('variable_here')

# In[2]:


print('This is a string {}'.format('INSERTED'))


# In[4]:


print('The {} {} {}'.format('fox', 'brown','quick'))


# the .format method, unless stipulated, will go sequentially.  Alternative below based on calling index position

# In[6]:


print('The {2} {1} {0}'.format('fox', 'brown','quick'))


# can also be called multiple times as below

# In[7]:


print('The {2} {2} {2}'.format('fox', 'brown','quick'))


# {} can be used to call the values of variables if they are assigned, as shown below

# In[10]:


print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))


# Float Formatting - allows you to adjust precision of numbers

# Flot Formatting syntax: "{value:width.precision f}"
# width: size of white space in string printed out
# precision: how specific in terms of number of decimal points past the decimal.

# In[11]:


result = 100/777


# In[12]:


result


# In[13]:


print('The result was {}'.format(result))


# In[14]:


print('The result was {r}'.format(r=result))


# In[19]:


print('The result was {r:1.5f}'.format(r=result))


# r is the value
# 10 is the width of the whitespace
# .5 is the precision of the float
# shown below

# In[21]:


print('The result was {r:10.5f}'.format(r=result))


# FORMATTED STRING LITERALS

# allows object values to be called directly in the code as demonstrated on below

# In[22]:


name = 'Jose'


# In[23]:


print('Hello, his name is {}'.format(name))


# In[26]:


#F-String literal below
print(f'Hello, his name is {name}')


# In[30]:


name = 'Sam'


# In[28]:


age = 3


# In[31]:


print(f'{name} is {age} years old')


# In[ ]:




