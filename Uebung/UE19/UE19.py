#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[131]:


import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense
import pandas as pd


# # 19.1.1 Import Data

# In[132]:


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.boston_housing.load_data(
    path="boston_housing.npz", test_split=0.2, seed=113
)


# In[133]:


print(x_train.shape)
x_train_df = pd.DataFrame(x_train)
x_train_df.info()
x_test_df = pd.DataFrame(x_test)


# In[134]:


y_train[:10]


# In[135]:


x_test.shape


# # 19.1.2 Create Model

# In[136]:


model = Sequential()
model.add(Dense(64, activation="relu", input_shape=(x_train_df.shape[1],)))
model.add(Dense(64, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])


# In[137]:


model.fit(x_train_df,y_train, epochs=80, batch_size=1, verbose=0)


# In[138]:


acc = model.evaluate(x_test, y_test)
print("MAE: "+str(acc[1]))


# # Normalizing the Data
# ### x_train_df boxplot

# In[139]:


#Boxplot der Daten:
x_train_df.boxplot()


# In[140]:


#Trainingsdaten normalisieren:
def normalizeTrainDF(df):
    df = df - df.mean()
    df = df / df.std(axis = 0, skipna = True)
    return df


# In[141]:


#Testdaten normalisieren:
def normalizeTestDF(trainDf, testDf):
    testDf = testDf - trainDf.mean()
    testDf = testDf / trainDf.std(axis = 0, skipna = True)
    return testDf


# ### normalized x_train_df

# In[142]:


#Normalisierte Traininsdaten:
x_train_normalized_df = normalizeTrainDF(x_train_df)
x_train_normalized_df.boxplot()


# ### normalized x_test_df

# In[143]:


#Normalisieren der TestDaten:
x_test_normalized_df = normalizeTestDF(x_train_df, x_test_df)
x_test_normalized_df.boxplot();


# # 19.1.3 Creating new Model with normalized Data

# In[144]:


normalized_model = Sequential()
normalized_model.add(Dense(64, activation="relu", input_shape=(x_train_normalized_df.shape[1],)))
normalized_model.add(Dense(64, activation="relu"))
normalized_model.add(Dense(1))

normalized_model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])


# In[151]:


normalized_model.fit(x_train_normalized_df,y_train, epochs=80, batch_size=1, verbose=0)


# In[152]:


normalized_model_acc = normalized_model.evaluate(x_test_normalized_df, y_test)
print("MAE: "+str(normalized_model_acc[1]))

