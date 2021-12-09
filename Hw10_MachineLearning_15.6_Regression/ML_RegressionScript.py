
#Name: Alejandra Hernandez
#Date: 11/24/2020
#Desc: Linear Regression for yearly avg tempp

''' How does the temp trend compare to the avg jan high temps?

    According to the data, seems to be ess correct. Not exact but close since the averages are much higher then the jan nyc temp.'''

#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


nyc = pd.read_csv(r'C:\Users\ahern\OneDrive\Desktop\noteBook\data.csv')


# In[15]:


nyc.columns = ['Date', 'Temperature', 'Anomaly']


# In[16]:


nyc.Date = nyc.Date.floordiv(100)


# In[17]:


nyc.head(3)


# In[18]:



# In[19]:


X_train, X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11)


# ## Training Linear Model
# 

# In[20]:

# In[21]:


linear_regression = LinearRegression()

# In[22]:

linear_regression.fit(X=X_train, y=y_train)

# In[23]:

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)


# #### Now, we can get the slope and intercept used in the y = mx + b calculation to make predictions.

# In[24]:

linear_regression.coef_

# In[25]:

linear_regression.intercept_

# #### Testing the cell
# In[26]:

predicted = linear_regression.predict(X_test)

# In[27]:

expected = y_test

# In[28]:

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')

# ### Predicting Future Temperatures and Estimating Past Temperatures

# In[29]:

predict = (lambda x: linear_regression.coef_ * x +
          linear_regression.intercept_)

# In[30]:

predict(2019)

# In[31]:

predict(2020)

# ### Visualizing Dataset with Regression Line

# In[32]:

# In[34]:

axes = sns.scatterplot(data=nyc, x='Date', y='Temperature',
                      hue='Temperature', palette='winter', legend=False)

# ### Making the line

# In[35]:
axes.set_ylim(10, 70)

# In[36]:

# In[38]:

x = np.array([min(nyc.Date.values), max(nyc.Date.values)])

# In[39]:

y = predict(x)

# In[41]:

# In[42]:

line = plt.plot(x, y)
plt.show()

# In[ ]: