#!/usr/bin/env python
# coding: utf-8

# # UE18.2 - MNIST2

# In[1]:


import tensorflow as tf
from tensorflow.keras.datasets import mnist
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[2]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[3]:


train_images_df = np.array(train_images)
train_images_df = train_images_df.reshape((1, 60000, 784))
df = pd.DataFrame(train_images_df[0])
df.head()


# In[4]:


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(512, activation="relu", input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
#model.add(tf.keras.layers.Dense(512, activation="relu"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()


# In[5]:


train_labels = tf.keras.utils.to_categorical(train_labels, 10)
train_labels.shape


# In[6]:


train_images = train_images.reshape((-1, 784))


# In[7]:


#model.fit(train_images, train_labels, epochs=5, batch_size=128)


# In[7]:


model_history = model.fit(train_images, train_labels, epochs=15, batch_size=64)
type(model_history.history)


# In[8]:


acc = model_history.history["accuracy"]
acc


# ## 18.2.1 Plot erstellen

# In[9]:


plt.plot(acc, 'b', label="Training")
plt.title("Korrektklassifizierungsrate Training")
plt.xlabel("Epochen")
plt.ylabel("Korrektklassifizierungsrate")
plt.legend()
plt.show()


# ## 18.2.2 

# In[10]:


test_images = test_images.reshape(test_images.shape[0], 784)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=10)


# In[ ]:


hist = model.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=15, batch_size=64)


# In[13]:


hist.history.keys()


# In[ ]:





# In[14]:


# plt.ylim((0.975,1))
plt.plot(hist.history["accuracy"], 'b', label="Training") 
plt.plot(hist.history["val_accuracy"], 'r', label="Validierung") 
plt.title("Korrektklassifizierungsrate Training/Validierung") 
plt.xlabel("Epochen") 
plt.ylabel("Korrektklassifizierungsrate") 
plt.legend()
plt.show()


# ## 18.3.1

# In[ ]:


y_pred = model.predict(test_images)
y_pred = np.argmax(y_pred, axis = 1)
test_labels = np.argmax(test_labels, axis = 1)

pd.crosstab(test_labels, y_pred, rownames = ["actual"], colnames = ["predicted"])


# In[ ]:


train_images[0]


# In[17]:


train_images = train_images / 255
train_images[0]


# In[18]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[19]:


train_images = train_images / 255


# In[20]:


test_images = test_images.reshape(test_images.shape[0], 784)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes = 10)
train_labels = tf.keras.utils.to_categorical(train_labels, 10)
train_images = train_images.reshape((-1, 784))


# In[21]:


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(512, activation="relu", input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()
hist = model.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=5, batch_size=128)


# In[22]:


plt.ylim((0.9,1))
plt.plot(hist.history["accuracy"], 'b', label="Training") 
plt.plot(hist.history["val_accuracy"], 'r', label="Validierung") 
plt.title("Korrektklassifizierungsrate Training/Validierung") 
plt.xlabel("Epochen") 
plt.ylabel("Korrektklassifizierungsrate") 
plt.legend()
plt.show()


# ## 18.3.4

# In[ ]:


model.save('model.h5')


# In[ ]:


from PIL import Image
import glob
images = []

for f in glob.iglob("C:/Users/tstei/KI4/UE18/TEIL4/PNG/*"):
    images.append(np.asarray(Image.open(f).convert("L")))

img = np.array(images, dtype=object)
img


# In[ ]:


train_images_df = img.reshape(1, 10 , 784)
df = pd.DataFrame(train_images_df[0])
df


# In[ ]:


train_labels = train_images_df[0]
train_labels.shape


# In[ ]:


train_labels = tf.keras.utils.to_categorical([0,1,2,3,4,5,6,7,8,9], num_classes = 10).astype(np.float32)
train_images = train_images_df[0].astype(np.float32)


# In[ ]:


model_history = model.fit(train_images, train_labels, epochs = 10, batch_size = 64)


# In[ ]:


y_pred = model.predict(train_images)
y_pred = np.argmax(y_pred, axis=1)
test_labels = np.argmax(train_labels, axis=1)

pd.crosstab(test_labels, y_pred, rownames=["actual"], colnames=["predicted"])

