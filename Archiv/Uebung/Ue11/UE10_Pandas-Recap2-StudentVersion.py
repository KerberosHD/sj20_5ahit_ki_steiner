#!/usr/bin/env python
# coding: utf-8

# # Übung 10 - Pandas Exercises 1
# Arbeiten Sie nachfolgenden Aufgabenstellungen durch und dokumentieren Sie, wenn notwendig, ihre Erkenntnisse. 

# In[1]:


import pandas as pd
import numpy as np


# ## Task 10.1
# Erstellen Sie basierend auf den 3 Listen `name`, `population` und `country` das *Dictionary* `cities`. Verwenden Sie die List-Bezeichner als *Keys*. Im nächsten Schritt gilt es mit dem *Dictionary* das *DataFrame* `citiy_df` zu erstellen. Gesuchte Ausgabe:
# 
# ```Python
#       name 	poulation   country
# 0 	London 	8615246 	England
# 1 	Berlin 	3562166 	Germany
# 2 	Madrid 	3165235 	Spain
# 3 	Rome 	2874038 	Italy
# 4 	Paris 	2273305 	France
# 5 	Vienna 	1805681 	Austria
# ...
# ```

# In[3]:


name = ["London", "Berlin", "Madrid", "Rome",
        "Paris", "Vienna", "Bucharest", "Hamburg",
        "Budapest", "Warsaw", "Barcelona",
        "Munich", "Milan"]

population = [8615246, 3562166, 3165235, 2874038,
                2273305, 1805681, 1803425, 1760433,
                1754000, 1740119, 1602386, 1493900,
                1350680]

country = ["England", "Germany", "Spain", "Italy",
            "France", "Austria", "Romania",
            "Germany", "Hungary", "Poland", "Spain",
            "Germany", "Italy"]
#Your code...
cities = {
    "name": name,
    "population": population,
    "country": country
}

city_df = pd.DataFrame(cities)
city_df


# ## Task 10.2
# Die Reihenfolge der Spalten kann bei der Erstellung des *DataFrames* festgelegt werden. Dazu dient das Schlüsselwort `columns` beim Instanziieren eines *DataFrames*. Ändern Sie diese, dass folgende Spaltenreihenfolge gegeben ist: *name* - *country* - *population*. Verwenden Sie hierzu die Liste `new_order`. Erstellen Sie mit `city_df` ein neues *DataFrame*.

# In[4]:


new_order = ["name", "country", "population"]

# Your code...
city_df = city_df[new_order]
city_df


# ## Task 10.3
# Man kann den Index entweder beim Erstellen eines *DataFrames* explizit definieren oder mit `set_index()` im Nachhinein ändern. Definieren Sie die Spalte *country* als neuen Index bei `city_df`. Wichtig: `set_index()` liefert ein neues DF-Objekt, was wir aber nicht möchten. Die Änderung soll in `city_df` direkt erfolgen!
# 
# Quelle: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html?highlight=set_index#pandas-dataframe-set-index

# In[5]:


# Your code...
city_df.set_index("country", inplace=True)
city_df


# ## Task 10.4
# Gesucht sind a) alle Städte Deutschlands und b) alle Städt Deutschlands und Frankreichs. Zur Erinnerung: Die Spalte *country* bildet den Index.
# 
# > **Remember**: `loc`und `iloc` durchsuchen ein *DataFrame* anhand des Index; es sind ausschließlich Werte der Index-Spalte zulässigt. Ignoriert man das, erhält man einen *Key Error*. Also bevor man loslegt, sollte man kurz innehalten und überlegen, was kann ich wie suchen und - hoffentlich - finden!
# 
# Den Index eines DataFrames kann man mit dem Property `index` ausgeben.

# In[6]:


# Your code...
germany = city_df.loc['Germany']
print(germany)

print("\n")

gerfran = city_df.loc[['Germany', 'France']]
print(gerfran)


# ## Task 10.5
# Gesucht sind alle jene Städte, deren *Population* > 2Mio. ist. 

# In[7]:


# Your code...
pop = (city_df['population'] > 2000000)
pop


# ## Task 10.6
# Aufgabenstellung 10.5 kann man auf mehrere Arten lösen. Legen Sie dar, war die `loc`-Varianten funktioniert - vor allem unter den in 10.5 diskutierten Gesichtspunkten?

# In[8]:


# Your code...
pop2 = city_df.loc[city_df['population'] > 2000000]
pop2


# ## Task 10.7
# Berechnen Sie die Gesamtsummer aller Städte.

# In[9]:


# Your code...
population_sum = city_df['population'].sum()
population_sum


# ## Task 10.8
# Fügen Sie dem *DataFrame* `city_df` die Spalte *area* mit den Werten der Liste `area` (Fläche in qkm) hinzu. Gesuchtes Ergebnis:
# 
# ```Python
#             name 	population 	area
# country 			
# England 	London 	8615246 	1572.00
# Germany 	Berlin 	3562166 	891.85
# Spain 	  Madrid 	3165235 	605.77
# Italy 	  Rome 	  2874038     1285.00
# France 	 Paris 	 2273305     105.40
# ```

# In[10]:


area = [1572, 891.85, 605.77, 1285,
        105.4, 414.6, 228, 755,
        525.2, 517, 101.9, 310.4,
        181.8]

# Your code...
city_df['area'] = area
city_df


# ## Task 10.9
# Sortieren Sie die Ausgabe nach *area*, und zwar in absteigener Reihenfolge. Verwenden Sie `sort_values()`. Quelle: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

# In[11]:


# Your code...
city_df.sort_values('area', inplace=True)
city_df


# ## Task 10.10
# Nehmen Sie spätestens jetzt den Abschnitt *Applying Functions* des Tutorials **Python Pandas Tutorial: A Complete Introduction for Beginners** (siehe Übung 09) durch. 
# 
# Ziel ist die Erstellung einer weiteren Spalte *megacities*, die für alle Städte, der *population* > 2Mio. ist, den Wert `True` enthält. Erstellen Sie hierzu die Funktion `def calc_megacities(population)`, in welcher die Abfrage zu implementieren ist. Das gesuchte Ergebnis (die unordentliche Darstellung ist dem JN geschuldet):
# 
# ```Python
#             name 	population 	area 	megacities
# country 				
# England 	London 	8615246 	1572.00 	True
# Italy       Rome 	2874038 	1285.00 	True
# Germany 	Berlin 	3562166 	891.85 	    True
# Germany 	Hamburg 1760433 	755.00 	    False
# Spain 	    Madrid 	3165235 	605.77 	    True
# ...
# ```

# In[12]:


# Your code...
def calc_megacities(population):
    if population > 2000000:
        return True
    else:
        return False
    
city_df['megactities'] = city_df['population'].apply(calc_megacities)
city_df


# ## Task 10.11
# 
# Diese Aufgabe basiert auf einem Dataset, dass je Messzeitpunkt *t* sechs Temperaturwerte (Sensor 1 bis Sensor 6) umfasst. Das Messintervall betrug 15 Minuten.
# 
# Ladens Sie a) das bereitgestellte Dataset *temperatures_with_NaN.csv* und geben Sie die Shape aus. 
# 
# Geben Sie b) die ersten 5 Zeilen aller Sensoren aus. Geben Sie c) ausschließlich die ersten 5 Zeilen der Sensoren 3 und 4 aus. 
# 
# Ermitteln Sie d) die Anzahl der NaN-Werte je Sensor sowie je Zeitpunkt *t*. **Hinweis**: Denken Sie an die Achsen-Thematik, diese ist bei `sum()` konfigurierbar (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html?highlight=sum#pandas.DataFrame.sum. Ermitteln Sie außerdem die Gesamtanzahl der *NaN*-Werte. Hierzu ein kleiner Tipp: "doppelt hält besser"! 
# 
# e) Der letzte Punkte dieser Aufgabe widmet sich der Ermittlung des Mittelwertes zum Zeitpunkt t (siehe neue Spalte *mean*). Das gesuchte Ergebnis ist:
# 
# ```Python
#             time 	sensor1 	sensor2 	sensor3 	sensor4 	sensor5 	sensor6 	mean
#     0 	06:00:00 	14.3 	    13.7 	  14.2 	  14.3 	   13.5 	  13.6 	 13.933333
#     1 	06:15:00 	14.5 	    14.5 	  14.0 	  15.0 	   14.5 	  14.7 	 14.533333
#     3 	06:45:00 	14.8 	    14.5 	  15.6 	  15.2 	   14.7 	  14.6 	 14.900000
#     4 	07:00:00 	15.0 	    14.9 	  NaN 	   15.6 	   14.0 	  15.3 	 14.960000
#     6 	07:30:00 	15.4 	    15.3 	  NaN 	   15.6 	   14.7 	  15.1 	 15.220000
# ```
# 
# **Vorgehensweise**
# 
# Es wird erstichtlich, dass z.B. die Messung zum Zeitpunkt t2 fehlt. Hintergrund ist, dass all jene Messungen entfernt wurden, die mehr als **einen** NaN-Wert aufwiesen. Das lässt sich mit `dropna()` überauseinfach bewerkstelligen (siehe Argument `thresh`). Hierbei ist die Gesamtanzahl der Spalten - also inkl. *time* - zu berücksichtigen! Entfernt man all jene Zeilen, die mehr als einen NaN-Wert enthalten, reduziert sich die Anzahl der Zeilen im Dataset auf 35.
# 
# Den zweiten und letzten Schritt, um diese Aufgabe zu bewerkstelligen, stellt die Ermittlung des Mittelwertes je Messzeitpunkt t dar. Das Ergebnis ist in die neue Spalte *mean* zu schreiben.

# In[13]:


#a)
dataset = pd.read_csv('temperatures_with_NAN.csv')
dataset.shape


# In[14]:


#b)
dataset.head(5)


# In[15]:


#c)
dataset[['sensor3', 'sensor4']].head(5)


# In[16]:


#d)
dataset.isnull().sum()


# In[17]:


#d)
dataset.set_index('time').isnull().sum(axis=1)


# In[18]:


#d)
dataset.isnull().sum().sum()


# In[19]:


#e)
dataset['mean'] = dataset.mean(axis=1)
dataset.head(5)

