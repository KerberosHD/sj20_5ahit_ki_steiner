#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix


# In[12]:


#17.1
df = pd.read_csv('dataset.csv')
df   


# In[13]:


df.info()


# In[14]:


df.mean()


# In[15]:


df.shape


# In[16]:


df.describe()


# In[17]:


#17.2
sns.countplot(df['Outcome'],label="Count")


# In[25]:


#17.3
sns.heatmap(df.corr(),cmap="Blues")


# In[19]:


#17.4
clf = RandomForestClassifier(max_depth=4, n_estimators=100)
X = df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y = df[['Outcome']].to_numpy().ravel()


# In[20]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1,test_size=0.30)
clf.fit(X_train,y_train)


# In[21]:


y_pred=clf.predict(X_test)
plot_confusion_matrix(clf, X_test, y_test)


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.3)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = SVC(random_state=0, kernel='rbf')
classifier.fit(X_train, y_train)


# In[28]:


y_pred = classifier.predict(X_test)
plot_confusion_matrix(classifier, X_test, y_test)


# In[ ]:




