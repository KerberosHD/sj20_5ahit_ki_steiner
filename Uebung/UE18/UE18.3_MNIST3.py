#!/usr/bin/env python
# coding: utf-8

# # UE18.3 - MNIST3

# In[35]:


import tensorflow as tf
from tensorflow.keras.datasets import mnist
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[36]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[37]:


train_images_df = np.array(train_images)
train_images_df = train_images_df.reshape((1, 60000, 784))
df = pd.DataFrame(train_images_df[0])
df.head()


# In[38]:


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(512, activation="relu", input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
#model.add(tf.keras.layers.Dense(512, activation="relu"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()


# In[39]:


train_labels = tf.keras.utils.to_categorical(train_labels, 10)
train_labels.shape


# In[40]:


train_images = train_images.reshape((-1, 784))


# In[41]:


#model.fit(train_images, train_labels, epochs=5, batch_size=128)


# In[42]:


model_history = model.fit(train_images, train_labels, epochs=10, batch_size=64)
type(model_history.history)


# In[43]:


acc = model_history.history["accuracy"]
acc


# ## 18.2.1 Plot erstellen

# In[44]:


plt.plot(acc, 'b', label="Training")
plt.title("Korrektklassifizierungsrate Training")
plt.xlabel("Epochen")
plt.ylabel("Korrektklassifizierungsrate")
plt.legend()
plt.show()


# ## 18.2.2 

# In[45]:


test_images = test_images.reshape(test_images.shape[0], 784)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=10)


# In[46]:


hist = model.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=10, batch_size=128)


# In[47]:


hist.history.keys()


# In[ ]:





# In[48]:


plt.ylim((0.9,1))
plt.plot(hist.history["accuracy"], 'b', label="Training") 
plt.plot(hist.history["val_accuracy"], 'r', label="Validierung") 
plt.title("Korrektklassifizierungsrate Training/Validierung") 
plt.xlabel("Epochen") 
plt.ylabel("Korrektklassifizierungsrate") 
plt.legend()
plt.show()


# ## 18.3.1

# In[49]:


y_pred = model.predict(test_images)
y_pred = np.argmax(y_pred, axis=1)
test_labels = np.argmax(test_labels, axis=1)

pd.crosstab(test_labels, y_pred, rownames=["actual"], colnames=["predicted"])


# ## 18.3.2

# In[50]:


train_images[0]


# In[51]:


train_images = train_images / 255
train_images[0]


# ## 18.3.3
# 

# In[79]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[75]:


train_images = train_images / 255


# In[80]:


test_images = test_images.reshape(test_images.shape[0], 784)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=10)
train_labels = tf.keras.utils.to_categorical(train_labels, 10)
train_images = train_images.reshape((-1, 784))


# In[81]:


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(512, activation="relu", input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
#model.add(tf.keras.layers.Dense(512, activation="relu"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()
hist = model.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=5, batch_size=128)


# In[82]:


plt.ylim((0.9,1))
plt.plot(hist.history["accuracy"], 'b', label="Training") 
plt.plot(hist.history["val_accuracy"], 'r', label="Validierung") 
plt.title("Korrektklassifizierungsrate Training/Validierung") 
plt.xlabel("Epochen") 
plt.ylabel("Korrektklassifizierungsrate") 
plt.legend()
plt.show()


# In[ ]:




