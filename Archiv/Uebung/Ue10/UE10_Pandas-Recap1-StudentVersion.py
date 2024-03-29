#!/usr/bin/env python
# coding: utf-8

# # Übung 8 - Pandas Exercises 1
# Arbeiten Sie nachfolgenden Aufgabenstellungen durch und dokumentieren Sie, wenn notwendig, ihre Erkenntnisse. 
# 
# ## Task 8.0
# Importieren Sie *pandas*.

# In[9]:


import pandas as pd

import numpy as np


# ## Task 8.1
# Erstellen Sie mit `data` ein *Series*-Objekt und geben Sie dessen Werte sowie Indizes aus. Zeigen Sie außerdem, dass
# - das erstellte Objekt vom Typ *Series*
# - die Werte ein vom Typ *numpy*
# - die Indizes vom Typ *RangeIndex*
# 
# ist/sind.

# In[12]:


data = np.array([11, 28, 72, 3, 5, 8])
s = pd.Series(data)
print(type(s))
print(s)
print(type(s.index))


# ## Task 8.2
# Erstellen Sie mit `quantities` eine *Series*. Verwenden Sie hierbei `fruits` als Indizes. Gesuchtes Ergebnis:
# 
# ```python
# apples      20
# oranges     23
# cherries    45
# pears       10
# dtype: int64
# ```
# > Ein Vorteil gegenüber NumPy-Arrays ist: Man kann beliebige Indizes verwenden! 

# In[24]:


fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 23, 45, 10]

fruit_price = pd.Series(quantities, index = fruits)
print(fruit_price)


# ## Task 8.3
# Man kann zwei *Series*-Objekte mit denselben Indizes addieren. Das Ergebnis ist ein neues *Series*-Objekt. Addieren sie die Quantities `q1` und `q2`. Bilden Sie außerdem die Summe der beiden *Series*-Objekte. Gesuchtes Ergebnis:
# 
# ```python
# apples      30
# oranges     36
# cherries    70
# pears       11
# dtype: int64
# Summe: 147
# ```

# In[23]:


fruits = ['apples', 'oranges', 'cherries', 'pears']

q1 = [20, 23, 45, 10]
q2 = [10, 13, 25, 1]

q1Series = pd.Series(q1, index = fruits)
q2Series = pd.Series(q2, index = fruits)

q3Series = q1Series + q2Series
print(q3Series)
print(sum(q3Series))


# ## Task 8.4
# Die Indizes müssen nicht zwingend identisch sein - Indizes können auch komplett verschieden sein! Erstellen zwei *Series'*, addieren Sie diese und geben Sie das neue *Series*-Objekt aus. Gesuchtes Ergebnis:
# 
# ```python
# apples      30.0
# cherries    70.0
# oranges     36.0
# peaches      NaN
# pears        NaN
# dtype: float64
# ```

# In[25]:


f1 = ['apples', 'oranges', 'cherries', 'pears']
f2 = ['apples', 'oranges', 'cherries', 'peaches']

q1 = [20, 23, 45, 10]
q2 = [10, 13, 25, 1]

q1Series = pd.Series(q1, index = f1)
q2Series = pd.Series(q2, index = f2)

q3Series = q1Series + q2Series
print(q3Series)


# ## Task 8.5
# Index-basierter Zugriff erfolgt mit (zwei) eckigen Klammern (z.B. `my_series['foo']` oder `my_series[['foo', 'bar']]`) Geben Sie a) die Anzahl der *Äpfel* aus. Geben Sie b) die Anzahl der *Äpfel*, *Orangen* und *Kirschen* aus. 

# In[32]:


fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 23, 45, 10]

fruitAmount = pd.Series(quantities, index = fruits)
print(fruitAmount[['apples']])
print(fruitAmount[['apples','oranges', 'cherries']])


# ## Task 8.6
# Ein Problem bei Aufgaben in der Datenanalyse besteht in fehlenden Daten. Gegeben ist das Dictionary `cities`, das für ausgewählte Städte die Einwohnerzahl bereithält. a) Erstellen Sie daraus eine *Series*-Objekt und geben Sie dieses aus. 

# In[35]:


cities = {
    'London': 8615246,
    'Berlin': 3562166,
    'Madrid': 3165235,
    'Rome': 2874038,
    'Paris': 2273305,
    'Vienna': 1805681,
    'Bucharest': 1803425,
    'Hamburg': 1760433,
    'Budapest': 1754000,
    'Warsaw': 1740119,
    'Barcelona': 1602386,
    'Munich': 1493900,
    'Milan': 1350690
}

citiesPanda = pd.Series(cities)
print(citiesPanda)


# Erstellen Sie b) zwei weitere *Series*-Objekte, die aber mit `my_cities1` und `my_cities2` neuen Indizes verwendet. Wie intrepretieren Sie das Ergebnis, was fällt Ihnen auf?
# 
# Es nimmt alle Werte aus Cities und alle die nicht in Cities  stehen bekommen keinen Wert

# In[51]:


my_cities1 = ['London', 'Paris', 'Zurich', 'Berlin', 'Stuttgart', 'Hamburg']

my_cities2 = ['London', 'Paris', 'Berlin', 'Hamburg']

my_cities1_Panda = pd.Series( citiesPanda, index = my_cities1)
my_cities2_Panda = pd.Series( citiesPanda, index = my_cities2)
print(my_cities1_Panda)
print()
print(my_cities2_Panda)


# `nan`steht für *not a number*. Das ist in unserem Fall als "fehlt" zu verstehen. Mit den Methoden `isnull`und `notnull` kann man auf fehlende Werte überprüfen. Führen Sie c) diese Überprüfung durch, sodass folgendes Ergebnis zu Buch steht:
# 
# ```Python
# London       False
# Paris        False
# Zurich        True
# Berlin       False
# Stuttgart     True
# Hamburg      False
# dtype: bool
# ```

# In[41]:


print(my_cities1_Panda.isnull())


# Filtern Sie d) die fehlende Werte mit `dropna()`. Gesuchtes Ergebnis:
# ```python
# London     8615246.0
# Paris      2273305.0
# Berlin     3562166.0
# Hamburg    1760433.0
# dtype: float64
# ```

# In[50]:


#my_cities1_Panda.dropna(inplace= True)
print(my_cities1_Panda.dropna())


# Oftmals will man die fehlenden Daten gar nicht filtern, sondern mit "passenden" Werten auffüllen. Eine Möglichkeit bietet sich mit der Methode `fillna()`. Man könnte bspw. lauter "0" eintragen. Setzen Sie e) diesen Vorschlag um:
# 
# ```Python
# London       8615246.0
# Paris        2273305.0
# Zurich             0.0
# Berlin       3562166.0
# Stuttgart          0.0
# Hamburg      1760433.0
# dtype: float64
# ```

# In[54]:


print(my_cities1_Panda.fillna(0))


# ## Task 8.7
# Ein *Dataframe* hat einen Zeilen- und Spaltenindex. Um mehrere *Series'* zusammenzufügen, stellt Pandas die `concat`-Methode zur Verfügung (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html). Erstellen Sie a) das Dataframe `shops_df`, indem Sie die 3 *Series'* zusammenfügen. Das Ergebnis gestaltet sich im ersten Schritt folgendermaßen:
# 
# ```Python
# 2014    2409.14
# 2015    2941.01
# 2016    3496.83
# 2017    3119.55
# 2014    1203.45
# 2015    3441.62
# 2016    3007.83
# 2017    3619.53
# 2014    3412.12
# 2015    3491.16
# 2016    3457.19
# 2017    1963.10
# dtype: float64
# ```

# In[58]:


#Die Jahre 2014, 2015, 2016 und 2017 erstellen, die als Index einer Series dienen:
years = range(2014, 2018)

shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)

shops_df = pd.concat([shop1, shop2, shop3])
print(shops_df)


# Das Ergebnis ist mehr oder weniger unbrauchbar. Der Grund: `concat` verwendet als Default-Wert für den *axis*-Paramter den Wert 0. Das bedeutet, es wird Zeile um Zeile (der jeweiligen *Series*) aneinandergefügt (vgl. NumPy-Einführung, Leserichtung bei 2D-Tensoren). Abhilfe schafft eine spaltenweise "Additiion" der einzelnen *Series'*. Die Umsetzung erfolgt mit dem Argument `axis=1` bei `concat`. Verwenden Sie b) das `axis=1`-Argument beim Zusammenfügen der *Series'*. Das Ergebnis:
# 
# ```Python
#             0        1        2
# 2014  2409.14  1203.45  3412.12
# 2015  2941.01  3441.62  3491.16
# 2016  3496.83  3007.83  3457.19
# 2017  3119.55  3619.53  1963.10
# ```

# In[60]:


shops_df = pd.concat([shop1, shop2, shop3], axis = 1)
print(shops_df)


# Die vorher erzielte Darstellungsform der Daten ist definitiv sinnvoller, einzig die Spaltennamen sind noch nicht das Gelbe vom Ei. Es ist bekannt, dass ein *DataFrame* über das **Property** `columns` verfügt. Diesem kann man neue Werte (z.B. als Liste) zuweisen. Weisen Sie c) dem DataFrame `shops_df` die neuen Spaltenbezeichner (siehe Liste `cities`) zu. Das Ergebnis:
# 
# ```Python
#          Wien     Graz  Salzburg
# 2014  2409.14  1203.45   3412.12
# 2015  2941.01  3441.62   3491.16
# 2016  3496.83  3007.83   3457.19
# 2017  3119.55  3619.53   1963.10
# ```

# In[67]:


cities = ['Wien', 'Graz', 'Salzburg'] 
shops_df.columns = cities
print(shops_df)


# Geben Sie d) die Inhalte der Spalte "Graz" aus und vergewissern Sie sich, ob die Spalte vom Typ *Series* ist.

# In[73]:


print(shops_df['Graz'])
print(type(shops_df['Graz']))

