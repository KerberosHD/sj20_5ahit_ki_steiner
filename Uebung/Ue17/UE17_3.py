#!/usr/bin/env python
# coding: utf-8

# # 17.3.1
# 
# |                     | qualitatives Merkmal | quantitatives Merkmal |
# |---------------------|:--------------------:|:---------------------:|
# | Körpergewicht       |           -          |          true         |
# | Autobahnbezeichnung |         true         |           -           |
# | Lieblingsfarbe      |         true         |           -           |
# | Taschengeld         |           -          |          true         |
# | Hausnummer          |           -          |          true         |

# # 17.3.2

# ![image.png](attachment:image.png)

# |                              | qualitatives Merkmal | quantitatives Merkmal |
# |------------------------------|:--------------------:|:---------------------:|
# | country                      |         true         |           -           |
# | beer_servings                |           -          |          true         |
# | spirit_servings              |           -          |          true         |
# | wine_servings                |           -          |          true         |
# | total_litres_of_pure_alcohol |           -          |          true         |
# | continent                    |         true         |           -           |

# # 17.3.3.

# In[1]:


import pandas as pd
import numpy as np


# In[16]:


diabetes_df = pd.read_csv('diabetes.csv')


# In[18]:


a= np.random.choice(a=['A','B','C'],size=len(diabetes_df.index))
diabetes_df['Demo']= a
diabetes_df["Demo"] = pd.Categorical(diabetes_df.Demo)

print(diabetes_df['Demo'].describe())
print(diabetes_df.info())

