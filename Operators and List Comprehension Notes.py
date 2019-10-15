#!/usr/bin/env python
# coding: utf-8

# Useful Operators

# Range() Operator
#     range() is a generator.
#     Generators are functions that generate data as opposed to saving it to memory.

# In[5]:


for num in range(0,10,2):
    print(num)


# In[6]:


list(range(0,11,2))


# Enumerate()

# In[9]:


index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))


# In[12]:


index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count +=1


# In[18]:


word = 'abcde'

for item in enumerate(word):
    print(item)


# In[20]:


word2 = 'bcdgef'

for index,letter in enumerate(word2):
    print(index)
    print(letter)
    print('\n')


# In[21]:


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']


# In[22]:


zip(mylist1,mylist2)


# In[23]:


for item in zip(mylist1,mylist2):
    print(item)


# In[24]:


list(zip(mylist1,mylist2))


# In[25]:


'x' in [1,2,3]


# In[26]:


'x' in ['x','y','z']


# In[27]:


'a' in 'a world'


# In[28]:


'mykey' in {'mykey':345}


# In[29]:


mylist = [1,3,5,677]


# In[30]:


min(mylist)


# In[31]:


max(mylist)


# In[32]:


from random import shuffle


# In[35]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[39]:


shuffle(mylist)


# In[40]:


mylist


# In[42]:


from random import randint


# In[44]:


randint(0,100)


# In[45]:


mynum = randint(0,15)


# In[46]:


mynum


# In[48]:


result = input ('Enter a number here: ')


# In[49]:


result


# In[50]:


type(result)


# In[51]:


int(result)


# In[52]:


type(result)


# In[53]:


type(int(result))


# List Comprehension Notes

# List comprehensions are an alternative to for loops along with .append()

# In[54]:


mystring = 'hello'


# In[56]:


mylist = []

for letter in mystring:
    mylist.append(letter)


# In[57]:


mylist


# In[58]:


mylist = [letter for letter in mystring]


# In[59]:


mylist


# In[60]:


mylist = [x for x in 'word']


# In[61]:


mylist


# In[63]:


mylist = [x for x in range(0,11)]


# In[64]:


mylist


# In[65]:


mylist =[x**2 for x in range(0,11)]


# In[66]:


mylist


# In[67]:


mylist = [x for x in range(0,11) if x%2 ==0]


# In[68]:


mylist


# In[70]:


celsius = [0,10,20,35.5]

fahrenheit = [((9/5)*temp +32) for temp in celsius]


# In[71]:


fahrenheit


# In[73]:


fahrenheit = []

for temp in celsius:
    fahrenheit.append(((9/5)*temp +32))


# In[74]:


fahrenheit


# If/Else statments in List Comprehension is possible, but makes it bulky and ugly

# In[75]:


results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]


# In[76]:


results


# Nested loops in list comprehensions

# In[77]:


mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)


# In[78]:


mylist


# In[79]:


mylist = [x*y for x in [2,4,6] for y in [1,10,100]]


# In[80]:


mylist


# In[ ]:




