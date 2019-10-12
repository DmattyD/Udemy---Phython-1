#!/usr/bin/env python
# coding: utf-8

# IF / ELIF / ELSE statement notes

# If, elif, else statements will only run when certain conditions are met

# Control Flow xyntax makes use of colons, indentation, and whitespace

# syntax of an if statement:
# 
# if some_condition:
#     #execute some code here

# syntax of an if/else statement:
#     
#     if some_condition:
#         #execute some code
#     else:
#         #do something else

# syntax of an if/else statement:
# 
# if some_condition:
#     #execute some code
# elif other_condition:
#     #run other code
# else:
#     #do something else

# In[5]:


hungry = True

if hungry: 
    print('Feed Me')


# In[7]:


hungry = False

if hungry:
    print('Feed Me')
else:
    print('I am not hungry')


# In[13]:


loc = 'Bank'

if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == 'Bank':
    print('Make Money!!!')
else:
    print('I don"t know')


# In[16]:


name = 'Sammyu'

if name == 'Frankie':
    print('Hello Frankie')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What"s your name?')


# In[ ]:




