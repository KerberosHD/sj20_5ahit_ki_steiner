#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.python.keras.datasets import mnist
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


from tensorflow.python.keras.layers import MaxPooling2D
(X_train, Y_train), (x_test, y_test) = mnist.load_data()


# In[3]:


X_train.shape


# In[4]:


X_train = X_train.reshape((X_train.shape[0],X_train.shape[1], X_train.shape[2],1))
X_train.shape
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], x_test.shape[2],1))


# In[5]:


Y_train = to_categorical(Y_train, 10)


# In[6]:


model = Sequential()
model.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
model.add(Flatten())
model.add(Dense(10, activation="softmax"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy",metrics=["accuracy"])


# In[7]:


model.fit(X_train, Y_train, epochs=5, batch_size=128 )


# In[8]:


predicted_numbers = model.predict(x_test)
predicted_numbers = np.argmax(predicted_numbers, axis=1)
#Accuracy:
print(f"MINST Accuracy: {accuracy_score(y_test, predicted_numbers) * 100}%")


# 20.2.2

# In[10]:


modelWithDense = Sequential()
modelWithDense.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
modelWithDense.add(MaxPooling2D(pool_size=(2,2)))
modelWithDense.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
modelWithDense.add(MaxPooling2D(pool_size=(2,2)))
modelWithDense.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
modelWithDense.add(Flatten())
modelWithDense.add(Dense(64, activation="relu"))
modelWithDense.add(Dense(10, activation="softmax"))
modelWithDense.compile(optimizer="rmsprop", loss="categorical_crossentropy",metrics=["accuracy"])


# In[11]:


model.fit(X_train, Y_train, epochs=5, batch_size=128 )


# In[12]:


predicted_numbers = model.predict(x_test)
predicted_numbers = np.argmax(predicted_numbers, axis=1)
#Accuracy:
print(f"MINST Accuracy: {accuracy_score(y_test, predicted_numbers) * 100}%")


# 20.2.3

# In[13]:


model.summary();


# In der Layer Spalte sieht man die verwendeten Layer.
# Der Conv2d Layer verringert die Output Shape um 2
# Der polling Layer halbiert die Output Shape
# Der Conv2d Layer führt die Kantenerkennung durch.
# Der polling Layer macht die Kanten ortsunabhängig
