#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img
from os import listdir
from os.path import isfile, join
from tensorflow.python.keras.layers import MaxPooling2D


# # UE 20.3 Convolutional Neuronal Networks 3 Cats and Dogs
# ## 20.3.1

# In[2]:


train = os.listdir('./train/')
test = os.listdir("./test1")
train_images_df= pd.DataFrame(train, columns=["filename"])
train_images_df["category"]= train_images_df["filename"].str.split(".", n=1,expand = True)[0]
print(train_images_df)


# ## 20.3.2

# In[3]:


#Es gibt 25000 Trainingsbilder:
print(train_images_df.shape[0])
#Das Dataset ist ausgeglichen:
print(train_images_df['category'].value_counts())


# ## 20.3.3

# In[4]:


def show_train_image(filename):
    img_file = load_img('./train/'+filename)
    plt.imshow(img_file)


# In[5]:


show_train_image('cat.0.jpg')


# ## 20.3.4

# In[6]:


model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dense(2, activation="softmax"))
model.compile(optimizer="rmsprop", loss="categorical_crossentropy",metrics=["accuracy"])


# ## Datenaufbereitung
# ### Train Test Split

# In[7]:


data = train_images_df.copy()
train_df, validation_df = train_test_split(data, test_size=0.20, random_state=1)
train_df = train_df.reset_index(drop=True)
validation_df = validation_df.reset_index(drop=True)
print(train_df.shape)
print(validation_df.shape)
print(train_df['category'].value_counts())
print(validation_df['category'].value_counts())


# ### Erstellung der Generatoren

# In[8]:


train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)


train_generator = train_datagen.flow_from_dataframe(
    dataframe = train_df,
    directory = "./train/",
    x_col = "filename",
    y_col = "category",
    target_size = (150,150),
    batch_size = 200,
    class_mode = "categorical")

validation_generator = validation_datagen.flow_from_dataframe(
    dataframe = validation_df,
    directory = "./train/",
    x_col = "filename",
    y_col = "category",
    target_size = (150,150),
    batch_size = 200,
    class_mode = "categorical")


# In[9]:


for data_batch, labels_batch in train_generator:
    print(data_batch.shape)
    print(labels_batch.shape)
    break


# In[10]:


history = model.fit(
    train_generator,
    steps_per_epoch = 100,
    validation_data = validation_generator,
    epochs=3)


# In[11]:


test_filenames = listdir("./test1")
test_df = pd.DataFrame({
    'filename': test_filenames
})
test_df.shape[0]


# In[12]:


test_gen = ImageDataGenerator(rescale=1./255)
test_generator = test_gen.flow_from_dataframe(
    test_df,
    directory="./test1/",
    x_col='filename',
    y_col=None,
    class_mode=None,
    target_size=(150,150),
    batch_size=32,
    shuffle=False )


# In[13]:


test_generator.reset()
pred=model.predict(test_generator, verbose=1)


# In[14]:


pred_rounded = np.argmax(pred, axis=-1)
test_df["category"] = pred_rounded
test_df.head(10)


# In[15]:


sample_test = test_df.head(18)
sample_test.head()
plt.figure(figsize=(12, 24))
for index, row in sample_test.iterrows():
    filename = row['filename']
    category = row['category']
    img = load_img("./test1/"+filename, target_size=(150,150))
    plt.subplot(6, 3, index+1)
    plt.imshow(img)
    plt.xlabel(f"{filename} ({category})")
plt.tight_layout()
plt.show()

