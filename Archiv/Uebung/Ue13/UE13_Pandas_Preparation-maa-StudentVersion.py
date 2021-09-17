#!/usr/bin/env python
# coding: utf-8

# # UE 13 - Pandas Datenaufbereitung
# 
# Diese Abschnitt beschäftigt sich schwerpunktmäßig mit den Pandas-Methoden `map()`, `apply()` und `applymap()`. 
# 
# > **Hinweis**: Fügen Sie neue Pandas-Befehle dem FactSheet.pdf hinzu.
# 
# Als Übungsgrundlage dient das *Iris Data Set* (Quelle: https://archive.ics.uci.edu/ml/datasets/Iris). Hierbei handelt es sich um einen Datensatz, der drei Irisarten (Iris setosa, Iris virginica und Iris versicolor) - also Blüten - unterscheidet.

# In[1]:


# Some libs are needed...
import pandas as pd
import numpy as np


# ## 13.0 - Sklearn-Installation
# 
# Installieren Sie *Scikit Learn* (Sklearn) via *Anaconda Prompt* (Quelle: https://sklearn.org/install.html). Scikit ist eine frei Python-Bibliothek zum maschinellen Lernen, die auch gleich einige Datasets (Quelle: https://sklearn.org/modules/classes.html#module-sklearn.datasets) bereitstellt.

# ## 13.1 - Iris-Dataset laden
# Laden Sie das Iris Dataset aus dem Scikit Learn-Paket. Hierzu stellt Scikit mit `load_iris()` eine eigene Methode bereit. Bevor Sie das Dokument *Some notes to the iris dataset* (siehe htl.boxtree.at/lehre) durchnehmen, begründen Sie, warum a) `iris.shape` dem Interprete nicht schmeckt?
# 
# Nehmen Sie b) das oben erwähnte Dokument durch und probieren Sie sich an der Variable `iris`.

# In[3]:


import sklearn
from sklearn import datasets

iris = datasets.load_iris()
iris
# Your Code...
iris.data
iris.keys()
iris['target_names']
iris['DESCR']
iris['feature_names']
iris['filename']


# ## 13.2 - DataFrame erstellen
# 
# Erstellen Sie a) das DataFrame `df_data` und geben Sie die ersten 5 Zeilen aus. Gefordert ist folgender Aufbau:
# 
# ```Python
#        sepal length (cm) 	sepal width (cm) 	petal length (cm) 	petal width (cm)
#     0 	   5.1 	                 3.5 	              1.4 	             0.2
#     1 	   4.9 	                 3.0 	              1.4 	             0.2
#     2 	   4.7 	                 3.2 	              1.3 	             0.2
#     3 	   4.6 	                 3.1 	              1.5 	             0.2
#     4 	   5.0 	                 3.6 	              1.4 	             0.2
# ```

# In[4]:


#Your code...
df_data = pd.DataFrame(iris.data, columns=iris.feature_names)
df_data.head(5)


# Fügen Sie b) dem DataFrame `df_data` die Spalte *Species* hinzu und erstellen Sie ein neues DataFrame mit dem Namen `iris_df`. Das gesuchte Ergebnis:
# 
# ```Python
#        sepal length (cm) 	sepal width (cm) 	petal length (cm) 	petal width (cm)       Species
#     0 	   5.1 	                 3.5 	              1.4 	             0.2               0
#     1 	   4.9 	                 3.0 	              1.4 	             0.2               0
#     2 	   4.7 	                 3.2 	              1.3 	             0.2               0
#     3 	   4.6 	                 3.1 	              1.5 	             0.2               0
#     4 	   5.0 	                 3.6 	              1.4 	             0.2               0
# ```
# 
# 

# In[5]:


#Your Code...
iris_df = df_data
iris_df['species'] = 0
iris_df.head(5)


# c) Verschaffen Sie sich einen Überblick, indem Sie folgende Fragen beantworten, und zwar auf Code-Eben:
# 
# - Über wie viele Zeilen verfügt das DataFrame `iris_df`?
# - Wie viele unterschiedliche Arten (Species) gibt es und wie viele umfasst die jeweilige Art?
# - Wie viele Zellen weisen `nan` auf?
# - Beurteilen Sie, ob die Mittelwertbildung der Spalte 'Species' Sinn ergibt.
# - Finden Sie heraus, ob eine Korrelation zwischen einzelen Features (Sepal length,..., Petal width) besteht.

# In[6]:


#Your Code....
iris_df.shape #150, 5
iris_df['species'].nunique()
iris_df.isnull().values.any()
iris_df['species'].mean() #Macht keinen Sinn weil es nur einen Wert gibt
iris_df.corr()


# ## 13.3 - apply, applymap und map
# 
# Arbeiten Sie das Tutorial https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff  durch. Abgabe der Code-Beispiele ist nicht notwendig.

# In[7]:


# Playground...
df = pd.DataFrame({ 'A': [1,2,3,4], 
                   'B': [10,20,30,40],
                   'C': [20,40,60,80]
                  }, 
                  index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])
df


# ## 13.4 Data preparation with apply, applymap or map
# 
# Überschreiben Sie a) die Spalte *Species*, wobei folgende Zuordnung gilt:
# 
# - 0 => SET
# - 1 => VER
# - 2 => VIR
# 
# Gesuchte Ergebnis:
# ```Python
#        sepal length (cm) 	sepal width (cm) 	petal length (cm) 	petal width (cm)       Species
#     0 	   5.1 	                 3.5 	              1.4 	             0.2               SET
#     1 	   4.9 	                 3.0 	              1.4 	             0.2               SET
#     2 	   4.7 	                 3.2 	              1.3 	             0.2               SET
#     3 	   4.6 	                 3.1 	              1.5 	             0.2               SET
#     4 	   5.0 	                 3.6 	              1.4 	             0.2               SET
# ```

# In[8]:


#Your Code...
def check_species(x):
    if x == 0:
        return 'SET'
    elif x == 1:
        return 'VER'
    elif x == 2:
        return 'VIR'
    return x

iris_df['species'] = iris_df['species'].apply(check_species)
iris_df.head(5)


# Erstellen Sie b) die neue Spalte `wide petal`, die das Ergebnis folgender Bedingung enhält:
# 
# Wenn `petal width (cm) >= 1.3` ist, dann soll die Zelle der jeweiligen Zeile den Wert 1 aufweisen, sonst 0. Setzen Sie eine `lambda`-Expression ein.

# In[9]:


#Your code...
iris_df['wide petal'] = iris_df['petal width (cm)'].apply(lambda x: 1 if x >= 1.3 else 0)
iris_df.head(5)


# Ermitteln Sie c) die *petal area* (Petal-Fläche) und speichern Sie diese in der neu zu erstellenden Spalte *petal area*. Setzen Sie eine `lambda`-Expression ein. 

# In[10]:


# You Code...
iris_df['petal area'] = iris_df.apply(lambda x: x['petal length (cm)'] * x['petal width (cm)'], axis=1)
iris_df.head(5)


# Logarithmieren Sie d) alle jene Zellen, die vom Typ `float`sind. Verwenden Sie `np.log()`. `lambda` is still your friend!

# In[11]:


# Your Code...
iris_df = iris_df.apply(lambda x: np.log(x) if isinstance(x, float) else x)
iris_df.head(5)

