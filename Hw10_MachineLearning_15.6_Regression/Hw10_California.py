#Name: Alejandra Hernandez
#Date: 11/24/2020

#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sklearn.datasets import fetch_california_housing
import pandas as pd


# In[8]:


california = fetch_california_housing()


# In[9]:


print(california.DESCR)


# In[10]:


pd.set_option('precision', 4)


# In[11]:


pd.set_option('max_columns', 9)


# In[12]:


pd.set_option('display.width', None)


# In[13]:


california_df = pd.DataFrame(california.data,
                            columns=california.feature_names)


# In[40]:


california_df.head()


# In[41]:


california.target_names


# In[42]:


california.feature_names


# In[43]:


california_df = pd.DataFrame(california.data, columns = california.feature_names)


# In[44]:


california_df.head()


# In[45]:


california_df.describe()


# In[46]:


import seaborn as sns


# In[47]:


sns.set_style('whitegrid')


# In[39]:


grid = sns.pairplot(data=california_df, vars=california_df.columns[0:4]
                   )


# In[ ]:



