#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [1,2,3]


# In[2]:


my_list2 =['string',100,23.3]


# In[9]:


len(my_list)


# In[4]:


len(my_list)


# In[5]:


mylist3 = ['one', 'two', 'three']


# Indexing a list:

# In[6]:


mylist3[1:]


# Concattinating a list:

# In[7]:


another_list = ['four', 'five']


# In[10]:


new_list = mylist3 + another_list


# In[11]:


new_list


# In[13]:


new_list


# Mutating a list:

# In[14]:


new_list[0] = 'ONE ALL CAPS'


# In[15]:


new_list


# Adding to the end of a list - appending()

# In[16]:


new_list.append('six')


# In[17]:


new_list


# In[19]:


new_list.append('seven')


# In[20]:


new_list


# Removing from the end of a list is done through .pop()

# In[21]:


new_list.pop()


# In[22]:


new_list


# In[23]:


popped_item = new_list.pop()


# In[24]:


popped_item


# In[25]:


new_list


# pop() from an index position

# In[26]:


new_list.pop(0)


# In[27]:


new_list


# Sort & Reverse

# In[28]:


new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]


# .sort() will sort the selected variable as a function

# In[29]:


new_list.sort()


# In[30]:


new_list


# .sort() does not return a value, so it cannot be assigned to a variable, as demonstrated below

# In[31]:


my_sorted_list = new_list.sort()


# In[32]:


type(my_sorted_list)


# In[34]:


new_list.sort()
my_sorted_list = new_list


# In[35]:


my_sorted_list


# In[36]:


num_list


# In[37]:


num_list.sort()


# In[38]:


num_list


# .reverse() method - does not return a value upon running, as show below

# In[39]:


num_list.reverse()


# In[40]:


num_list


# In[ ]:




