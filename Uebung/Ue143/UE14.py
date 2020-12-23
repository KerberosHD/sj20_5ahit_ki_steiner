#!/usr/bin/env python
# coding: utf-8

# In[65]:


#Imports
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#Create a classifier of type "RandomForest"
clf = RandomForestClassifier(max_depth=80, n_estimators=100)
print('ready')


# In[2]:


#Datenerstellung:
iris = datasets.load_iris()
df_target = pd.DataFrame(iris['target'],columns=['Species'])
df_data = pd.DataFrame(iris['data'], columns=iris.feature_names)
df_data = pd.concat([df_data,df_target], axis=1)
print(df_data)


# In[3]:


#Daten aufbereiten:
X = df_data[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']]
y = df_data[['Species']].to_numpy().ravel()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)


# In[66]:


#Trainieren:
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print(y_pred)


# In[5]:


#Test:
df_result = pd.DataFrame({'predicted':  y_pred,'actual':y_test})
df_result['correct'] = df_result.apply(lambda x: 1 if x['predicted'] == x['actual'] else 0, axis=1)
#Result:
df_result


# In[67]:


#Accuracy:
print(f"Accuracy: {round(df_result['correct'].sum() / len(df_result) * 100,2)}%")


# In[68]:


#Accuracy mit sklearn:
print(f"Accuracy: {round(accuracy_score(y_test,y_pred)*100,2)}%")


# In[64]:


#Anwendung des Classifiers:
clf.predict([[6, 3.0, 5.5, 1.8]])

