#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[6]:


import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt


# # zum Aufwärmen

# In[112]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr)


# In[113]:


arr = arr.reshape(3,3)

print(arr)


# In[114]:


mean = np.mean(arr, axis=0)

print(mean)


# # UE 20 Convolutional Neuronal Networks 1
# ## 20.1.1

# In[111]:


# Bei RGB Bildern wäre eine Shape von (28,28,3) nötig, weil r g b drei Schichten sind


# In[105]:


#Modell erstellen

model = Sequential()
model.add(Conv2D(10, kernel_size=(3,3), activation="relu",input_shape=(28,28,1)))
print(model.output_shape)
model.add(Flatten())
print(model.output_shape)
model.add(Dense(512, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy",metrics=["accuracy"])


# In[106]:


#Daten aufbereiten:
#Daten importieren:

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#Reshape:
train_images = train_images.reshape(train_images.shape[0],train_images.shape[1],train_images.shape[2],1)
test_images = test_images.reshape(test_images.shape[0], test_images.shape[1], test_images.shape[2], 1)
#Pixelwerte zwischen 0 und 1 bringen

train_images = train_images / 255
test_images = test_images / 255
#Categorize Labels:
train_labels = to_categorical(train_labels, 10)
test_labels = to_categorical(test_labels, 10)


# In[107]:


#Predict Images:
predicted_minst_numbers = model.predict(test_images)
predicted_minst_numbers = np.argmax(predicted_minst_numbers, axis=1)
test_labels = np.argmax(test_labels, axis=1)
#Accuracy:
print(f"MINST Accuracy: {accuracy_score(test_labels, predicted_minst_numbers) * 100}%")


# ## 20.1.3

# In[110]:


#Den Flatten Layer braucht man um einen Mehrdimensionalen Input in einen Vektor umzuwandeln
#Wie man oben beim erstellen des Models sehen kann wird von (None, 26, 26, 10) zu (None, 6760) umgewandelt


# ## 20.1.4

# In[108]:


#Filter aus dem Model extrahieren
data = K.eval(model.layers[0].weights[0])
print(data.shape)
print(data)


# In[109]:


for i in range(data.shape[3]):
    #print(f"Filter {i}:")
    plt.imshow(data[:,:,:,i].reshape(3,3))
    plt.title(f"Filter {i}:")
    plt.show()

