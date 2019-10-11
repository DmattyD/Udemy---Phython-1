#!/usr/bin/env python
# coding: utf-8

# Dictionaries:
# Dictionaries are unordered mappings for storing objects.
# Dictionaries use a key-value pair as opposed to a sequence found in lists.
# 
# The key-value pair allows users to quickly grab objects without needing to know an index location.

# Call the key, return the value

# syntax: {'key1':'value1','key2':'value2'.....}

# Dictionary vs List.
# 
# Dictionaries: Objects retrieved by key name.  Unordered and cannot be sorted.
# 
# 
# Lists: Objects retrieved by location.  Can be indexed or sliced.

# In[1]:


my_dict = {'key1':'value1','key2':'value2'}


# In[2]:


my_dict


# In[4]:


my_dict['key1']


# In[6]:


prices_lookup = {'apple':2.99, 'oranges':1.99,'milk': 5.90}


# In[7]:


prices_lookup['apple']


# Dictionaries can hold lists or other dictionaries

# In[8]:


d = {'k1':123,'k2':[0,1,2], 'k3':{'insideKey':100}}


# In[9]:


d['k2']


# In[10]:


d['k3']


# Can stack or go multiple layers deep by adding the second key in square brackets after selecting the first key to be returned.

# In[ ]:


d['k3']['insideKey']


# Can index a list within a dictionary by selecting the index position to return after calling the key and then selecting the index position in [] brackets after

# In[12]:


d['k2'][2]


# In[13]:


d2 = {'key1':['a','b','c']}


# In[15]:


d2


# Grab the letter 'c' and make it uppercase

# In[17]:


d2['key1'][2].upper()


# In[18]:


d2


# In[19]:


d2['key1']


# In[20]:


d2['key1'][1]


# In[21]:


d2['key1'][2].upper()


# In[22]:


d = {'k1': 100, 'k2':200}


# In[23]:


d


# Insert a new key-value pair to a dictionary.  Call the dictionary, then [] with key inside, = to desired value

# In[24]:


d['k3'] = 300


# In[25]:


d


# Mutate a key-value pair by calling the key and assigning it a new value

# In[26]:


d['k1']


# In[27]:


d['k1'] = 'New Value'


# In[28]:


d


# Useful methods:
# 
# d.keys() - returns the keys.
# 
# d.values() - returns the values.
# 
# d.items() - returns the pairings (as tuples)

# In[29]:


d.keys()


# In[30]:


d.values()


# In[31]:


d.items()


# In[ ]:




