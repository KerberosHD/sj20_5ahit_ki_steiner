#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


cosine_similarity(np.array([4,0,5,3,5,0,0]).reshape(1,-1),                   np.array([0,4,0,4,0,5,0]).reshape(1,-1))


#  Task 1

# In[3]:


cosine_similarity(np.array([4,0,5,3,5,0,0]).reshape(1,-1),                  
                  np.array([2,0,2,0,1,0,0]).reshape(1,-1))


# Task 2

# In[4]:


cosine_similarity(np.array([-0.25,0,0.75,-1.25,0.75,0,0]).reshape(1,-1),                  
                  np.array([0,-0.33,0,-0.33,0,0.67,0]).reshape(1,-1))


# Task 3

# In[5]:


# functions
def recenter(matrix):
    matrix_mean = round(matrix[matrix.nonzero()].mean(), 2)
    recentered_values = [round(x - matrix_mean, 2) if x != 0 else x for x in matrix]
    return recentered_values

def checkSum(matrix):
    if(round(sum(matrix)) == 0):
        print("checkSum: success")
    else:
        print("checkSum: fail")


# In[6]:


# customers
cust_a = np.array([4,0,5,3,5,0,0])
cust_b = np.array([0,4,0,4,0,5,0])
cust_c = np.array([2,0,2,0,1,0,0])
cust_d = np.array([0,5,0,3,0,5,4])


# test the functions

# In[7]:


cust_a_recentered = recenter(cust_a)
print(cust_a_recentered)
checkSum(cust_a_recentered)


# In[8]:


cust_b_recentered = recenter(cust_b)
print(cust_b_recentered)
checkSum(cust_b_recentered)


# In[9]:


cust_c_recentered = recenter(cust_c)
print(cust_c_recentered)
checkSum(cust_c_recentered)


# In[10]:


cust_d_recentered = recenter(cust_d)
print(cust_d_recentered)
checkSum(cust_d_recentered)

