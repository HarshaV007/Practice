#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[3]:


import pandas as pd
from collections import Counter


# In[27]:


with open('D:/download_data/QTX_Programming Question/InputText') as f:
    contents = f.read()
    print(contents)


# In[29]:


my_str = contents
print(Counter(my_str))
my_str.lower()


# In[37]:


data1_split=my_str.split()


# In[76]:


from pandas import DataFrame
df = pd.DataFrame({'word':data1_split})
print (df)


# In[79]:


df['word']=df['word'].str.replace('.','').str.replace(')','').str.replace(',','').str.replace('(','')


# In[80]:


print(df)


# In[82]:


df = df.applymap(lambda s:s.lower() if type(s) == str else s)


# In[83]:


print(df)


# In[90]:


df['Vowels'] = df.word.str.count('[aeiou]')


# In[91]:


df['Consonant'] = df.word.str.count('[a-z]') - df['Vowels']


# In[92]:


print(df)


# In[111]:


from collections import Counter
from string import ascii_uppercase

df = df[['word']].join(pd.DataFrame([Counter(word) for word in df['word'].str.upper()])
                       .reindex(list("AEIOU"), axis=1).fillna(0).astype(int))


# In[112]:


print(df)


# In[114]:


df['Vowels'] = df.word.str.count('[aeiou]')


# In[116]:


df['Consonant'] = df.word.str.count('[a-z]') - df['Vowels']


# In[118]:


print(df)


# In[120]:


df.to_excel ('D:/download_data/QTX_Programming Question/output2.xlsx', index = False, header=True)


# In[ ]:




