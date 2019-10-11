#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nthis is the second line\nthis is the third line')


# In[2]:


myfile = open('myfile.txt')


# In[3]:


myfile= open('whoops.txt')


# In[4]:


#print the working directory
pwd


# In[5]:


pwd


# In[6]:


myfile = open('myfile.txt')


# .read() will return all of the text from a .txt file as a string.
# 
# lines will be sepearated by \n

# In[7]:


myfile.read()


# after reading a file, it must be reset, or it will keep the cursor at the end of the file

# In[8]:


myfile.read()


# In[9]:


myfile.seek(0)


# In[10]:


myfile.read()


# In[11]:


myfile.seek(0)


# In[12]:


contents = myfile.read()


# In[13]:


contents


# In[14]:


myfile.seek(0)


# read the lines of a txt file with readlines()

# In[15]:


myfile.readlines()


# File Locations
# 
# to open a file from another location, provide the full file path.  
# 
# windows use double "\\\"'s as by default '\\' is an escape character between folders
# 
# macOs and Linux use / between folders

# Best practices is to use .close() when done to prevent errors

# In[16]:


myfile.close()


# The below code will place the contents of a txt file into a variable that can be called, but doesn't open the file, thus preventing errors

# In[18]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


# In[19]:


contents


# In[20]:


with open('myfile.txt',mode = 'r') as myfile:
    contents = myfile.read()


# In[23]:


contents


# Reading, Writing, Appending Modes for .txt files
# 
# mode = 'r' is read only
# 
# mode = 'w' is write only (will overwrite files or create a new one)
# 
# mode = 'a' is append only (will add to files)
# 
# mode = 'r+' is reading and writing
# 
# mode = 'w+' is writing and reading (Overwrites existing files or creates a new file)

# In[24]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[26]:


with open('my_new_file.txt', mode='r') as f:
          print(f.read())


# In[27]:


with open('my_new_file.txt', mode='a') as f:
    f.write('FOUR ON FOURTH')


# In[28]:


with open('my_new_file.txt', mode='r') as f:
          print(f.read())


# In[30]:


with open('abfnioand.txt',mode='w') as f:
    f.write('I CREATED THIS FILE!')


# In[31]:


with open('abfnioand.txt', mode='r') as f:
    print(f.read())


# In[ ]:




