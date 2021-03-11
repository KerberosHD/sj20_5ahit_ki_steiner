#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist 
import pandas as pd 


# In[2]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[3]:


train_images.shape[0]


# In[4]:


train_images_df = pd.DataFrame(train_images.reshape(train_images.shape[0], 784))
train_images_df.head()


# In[5]:


train_images = train_images.reshape(train_images.shape[0], 784)


# In[6]:


train_images.shape


# In[7]:


train_labels


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


plt.imshow(train_images[0].reshape(28,28), cmap="gray_r")
plt.show()


# In[10]:


from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


# In[11]:


model = Sequential()
model.add(Dense(512, activation="relu", input_shape=(784,)))
model.add(Dense(10, activation="softmax"))

model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]) 

model.summary()


# In[12]:


train_labels = to_categorical(train_labels, 10)


# In[16]:


train_labels.shape


# In[17]:


model.fit(train_images, train_labels, epochs=5, batch_size=128) 


# In[19]:


test_images = test_images.reshape(test_images.shape[0], 784)
test_images.shape


# In[21]:


test_labels = to_categorical(test_labels, 10)
test_labels.shape


# In[22]:


model.evaluate(test_images, test_labels)


# ### Vgl. RFC

# In[23]:


y_pred = model.predict(test_images)


# In[33]:


y_pred[2]


# In[28]:


test_labels[1]

