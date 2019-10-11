#!/usr/bin/env python
# coding: utf-8

# Tuples

# Tuples are similar to lists, but they are IMMUTABLE.
# 
# Once an element is inside a tuple, it cannot be reassigned.
# 
# Tuples use parenthesis: (1,2,3)

# In[1]:


t = (1,2,3)


# In[2]:


mylist = [1,2,3]


# In[3]:


type(t)


# In[4]:


type(mylist)


# In[5]:


t


# In[6]:


t[0]


# Index() and Count() methods

# In[7]:


t = ('a', 'a', 'b')


# In[8]:


t


# .count() will count the total number of occurrences in the tuple

# In[10]:


t.count('a')


# .index() will only return the first occurrence of the value

# In[11]:


t.index('a')


# In[12]:


t.index('b')


# In[13]:


t


# In[15]:


mylist


# In[16]:


mylist[0] = 'NEW'


# In[17]:


mylist


# In[18]:


t[0] = 'NEW'


# Sets
# 
# Sets are unordered collections of unique elements.
# 
# There can only be one representative of the same object.

# In[19]:


myset = set()


# In[20]:


myset


# In[21]:


myset.add(1)


# In[22]:


myset


# In[23]:


myset.add(2)


# In[24]:


myset


# CANNOT add a duplicate object

# In[ ]:


myset.add(2)


# In[26]:


myset


# In[27]:


set('Mississippi')


# Booleans
# 
# True or False operators
# 
# this deal with control flow and logic

# In[28]:


True


# In[30]:


False


# In[31]:


type(False)


# In[32]:


2 > 4


# In[33]:


1 == 1


# In[34]:


b = None


# In[35]:


b


# In[ ]:




