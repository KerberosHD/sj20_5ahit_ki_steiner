#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import sklearn
from sklearn.ensemble import RandomForestClassifier
from scipy import stats
from sklearn.svm import SVC # "Support vector classifier"
from sklearn import metrics
from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import plot_confusion_matrix


# In[2]:


diabetes_df = pd.read_csv('diabetes.csv')


# In[ ]:


X= pd.DataFrame(data=diabetes_df.loc[:,diabetes_df.columns !='Outcome'])
Y= diabetes_df['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=2)

model = SVC(kernel='rbf')

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

#Finding the Accuracy

print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))


# In[32]:


param_grid = [
  {'C': [0.001, 0.01, 0.1, 1, 10], 'gamma': [0.001, 0.01, 0.1, 1], 'kernel': ['rbf', 'linear', 'sigmoid']}
 ]


# In[33]:


grid_search = GridSearchCV(estimator = model, param_grid = param_grid, n_jobs = -1, verbose = 2)


# In[ ]:


grid_search.fit(X_train, Y_train)


# In[ ]:


print(grid_search.best_params_)
print(grid_search.best_score_)


# In[10]:


param_gridRF = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 150, 200]
}


# In[12]:


clf = RandomForestClassifier(max_depth=5, n_estimators=100)
x=pd.DataFrame(data=diabetes_df.loc[:,diabetes_df.columns !='Outcome'])
y= diabetes_df['Outcome']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=1)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracity =sklearn.metrics.accuracy_score(y_test, y_pred, normalize=True, sample_weight=None)


# In[ ]:


grid_searchRF = GridSearchCV(estimator = clf, param_grid = param_gridRF, n_jobs = -1, verbose = 2)
grid_searchRF.fit(x_train, y_train)


# In[ ]:


print(grid_searchRF.best_params_)
print(grid_searchRF.best_score_)


# In[ ]:


df_meancalc= diabetes_df.copy()
df_meancalc = df_meancalc.replace(0, np.nan)
df_meancalc['Outcome']= diabetes_df['Outcome']
means= df_meancalc.groupby('Outcome').median()

diabetes_df.loc[(diabetes_df.Glucose==0) & (diabetes_df.Outcome==0), 'Glucose' ]=means.loc[0].loc['Glucose']
diabetes_df.loc[(diabetes_df.Glucose==0) & (diabetes_df.Outcome==1), 'Glucose' ]=means.loc[1].loc['Glucose']

diabetes_df.loc[(diabetes_df.BloodPressure==0) & (diabetes_df.Outcome==0), 'BloodPressure' ]=means.loc[0].loc['BloodPressure']
diabetes_df.loc[(diabetes_df.BloodPressure==0) & (diabetes_df.Outcome==1), 'BloodPressure' ]=means.loc[1].loc['BloodPressure']

diabetes_df.loc[(diabetes_df.SkinThickness==0) & (diabetes_df.Outcome==0), 'SkinThickness' ]=means.loc[0].loc['SkinThickness']
diabetes_df.loc[(diabetes_df.SkinThickness==0) & (diabetes_df.Outcome==1), 'SkinThickness' ]=means.loc[1].loc['SkinThickness']

diabetes_df.loc[(diabetes_df.Insulin==0) & (diabetes_df.Outcome==0), 'Insulin' ]=means.loc[0].loc['Insulin']
diabetes_df.loc[(diabetes_df.Insulin==0) & (diabetes_df.Outcome==1), 'Insulin' ]=means.loc[1].loc['Insulin']

diabetes_df.loc[(diabetes_df.BMI==0) & (diabetes_df.Outcome==0), 'BMI' ]=means.loc[0].loc['BMI']
diabetes_df.loc[(diabetes_df.BMI==0) & (diabetes_df.Outcome==1), 'BMI' ]=means.loc[1].loc['BMI']


# In[ ]:


X= pd.DataFrame(data=diabetes_df.loc[:,diabetes_df.columns !='Outcome'])
Y= diabetes_df['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=2)

model = SVC(kernel='rbf')

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)


# In[ ]:


grid_search = GridSearchCV(estimator = model, param_grid = param_grid, n_jobs = -2, verbose = 3)


# In[ ]:


grid_search.fit(X_train, Y_train)


# In[ ]:


clf = RandomForestClassifier(max_depth=5, n_estimators=100)
x=pd.DataFrame(data=diabetes_df.loc[:,diabetes_df.columns !='Outcome'])
y= diabetes_df['Outcome']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=1)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracity =sklearn.metrics.accuracy_score(y_test, y_pred, normalize=True, sample_weight=None)


# In[ ]:


grid_searchRF = GridSearchCV(estimator = clf, param_grid = param_gridRF, n_jobs = -2, verbose = )
grid_searchRF.fit(x_train, y_train)


# In[ ]:


print(grid_searchRF.best_params_)
print(grid_searchRF.best_score_)


# In[23]:


print(grid_search.best_params_)
print(grid_search.best_score_)


# In[24]:


plot_confusion_matrix(grid_searchRF, x_test, y_test)


# In[25]:


plot_confusion_matrix(grid_search, X_test, Y_test)

