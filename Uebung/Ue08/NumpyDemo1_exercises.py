#!/usr/bin/env python
# coding: utf-8

# # NumPy - erste Schritte
# Bei **Numpy** (https://numpy.org/doc/stable/index.html) handelt es sich um ein Modul, welches grundlegende Datenstrukturen (mehrdimensionale Arrays und Matrizen) zur Verfügung stellt, die auch *Matplotlib*, *SciPy* und *Pandas* benutzt werden. Die Bezeichnung NumPy ist eine Abkürzung für "Numerical Python" (Numerisches Python). Was damit gemeint ist, werden die nachfolgenden Übung verdeutlichen. 
# 
# Wissenswert ist, dass ein großer Teil von NumPy in C geschrieben worden ist. Die kompilierten mathematischen und numerischen Funktionen und Funktionalitäten werden somit mit "größter" Geschwindigkeit ausgeführt..

# In[5]:


import numpy as mp #Die Konvention ist np nicht mp


# In[5]:


#Definition einer klassischen Python-Liste mit z.B. Temperaturwerten
c_values = [20.1, 20.8, 21.9, 22.5, 22.7]
print(c_values)

#aus einer Liste kann man ein sog. NumPy-Array erzeugen:
c = mp.array(c_values)
print(c, type(c))


# In[8]:


#Berechne die Temperaturwert in "Fahrenheit", und zwar mit klassischen Python: C * 1.8 +32

#Lösung mit einer sog. List Comprehension:
f_values = [val * 1.8 + 32 for val in c_values]
print(f_values)


#Klassische Lösung mit for Loop
f_values = []
for temp in c_values:
    f_values.append(float(temp * 1.8 +32))
print(f_values)


# In[11]:


print(c * 1.8 +32) # mit numpy können numerische Operationen an einem array angewendet werden
print(c) # c wird nicht verändert


# In[ ]:


# Genau genommen, ist 'c' eine Instanz der Klasse numpy.ndarray!
type(c)


# ## Grafische Darstellung der Werte
# Um zu demonstrieren, wie schnell mithilfe von *Matplotlib* ansprechende Diagramme erstellt werden können, geben wir die oben erstellten Temperaturwerte mit diesem Modul aus. Eine detaillierte Besprechung des Moduls erfolgt später. 

# In[15]:


#im Jupyter Notebook prüfen, welche Variante funktioniert (mit oder ohne 'inline')
#%matplotlip inline   //vielleicht braucht man dass
import matplotlib.pyplot as plt

plt.plot(c)
plt.show()


# Die Werte des Arrays `c` dienen als Grundlage für die Ordinate (y-Achse). Die Indizes sind der Abszisse (x-Achse) zu entnehmen. 

# ## Weitere Funktionen zum Erzeugen von Arrays
# NumPy bietet Funktionen, um Intervalle mit Werten zu erzeugen, deren abstände gleichmäßig verteilt sind. 
# 
# 
# ### arange
# **arange** liefert gleichmäßig verteilte Werte innerhalb eines Intervalls zurück. Mit Interger-Werte ist diese Funktion Quasi-Äquivalent" mit der Python-Funktion `range`

# In[22]:


a = mp.arange(0, 6, 2, dtype="uint8") # Das Intervall inkludiert den Start-, aber nicht mehr den Stopwert!
print(a, type(a))   #u heißt dass es unsigned ist als 255 sonst wäre es signed : -127 bis 128
print(a.dtype)


# ### Nulldimensionale Arrays
# Nulldimensionale Arrays werden auch **Skalare** oder **0-D-Tensor** genannt. Hierbei handelt es sich um einen Tensor, der nur **einen Wert** enthält. Mit `ndim` erhält man die Dimension des Tensors, mit `dtype` den Typ des Arrays. Nachdem NumPy C-basiert ist, sind viel mehr Datentypen (z.B. int8, int16 etc.) möglich.

# In[7]:


x = mp.array(27)
print("x:", x)
print("Typ von x:", type(x))
print("Dimension von x:", x.ndim) # :)
print("Dimension von x:" , mp.ndim(x))
print("Datentyp der Werte von x:", x.dtype)


# ### Eindimensionales Array
# Ein Array von Zahlen wird als **Vektor** oder **1-D-Tensor** bezeichnet. Ein 1-D-Tensor besitzt genau 1 Achse.

# In[8]:


x = mp.array([12, 4, 23, 14])
print("x:", x)
print("Dimension von x:" , mp.ndim(x))


# ### Zweidimensionale Arrays
# Ein Array von Vektoren nennt man **2-D-Tensor** oder **Matrix**. Eine Matrix besitzt 2 Achsen, die oft als *Zeilen* und *Spalten* bezeichnet werden. Die Inhalte der ersten Achse heißen Zeile, die Inhalte der zweitem Spalten. 

# In[13]:


#von oben nach unten ist die axis = 0
# von links nach rechts ist das die axis 1
# Diese Information ist beim Zugriff auf die Datenstruktur wichtig => ob Zugriff spalten - oder Zeilenweise erfolgen soll!
x = mp.array([[12, 4, 23, 14, 56], 
             [13, 5, 24 ,15 , 57],
             [14, 6, 25, 16, 58]])
print("x:", x)
print("Dimension von x:" , x.ndim)


# > 3-D-Tensoren und höherdimensionale Tensoren sehen wir uns zu einem späteren Zeitpunkt an!

# ### Shape bzw. die Gestalt eines Arrays
# 
# Die Funktion `shape` liefert Informationen über die Gestalt eines Arrays. De Return-Wert ist ein Integer-Tupel. Vereinfacht ausgedrückt, ist liefert `shape` die Anzahl der Elemente pro Achse (Dimensionen). Im obigen Bsp. ist die Shape gleich **(3,5)**. Das bedeutet, dass wir **3 Zeilen** und **5 Spalten** haben. 

# In[14]:


print(x.shape)


# > Der Output von `shape`sagt auch etwas über die Reihenfolge, mit der die Indizes ausgeführt werden, aus, dh. zuerst die Zeilen, dann die Spalten (und dann gegebenenfalls noch weitere Dimensionen).

# Jetzt ein wenig *magic*: Mit `shape` kann man die Gestalt eines Arrays verändern.

# In[ ]:


x.shape = (5,3)


# ## Matrizenmultiplikation und Skalarprodukt
# In englischen Texten wird häufig vom 'dot product' gesprochen. Mathematisch versteht man darunter das Skalarprodukt von zwei Vektoren. Um das Skalarprodukt zu berechnen, stellt NumPy die `dot`-Funktion zur Verfügung. **Hinweis**: Die `dot`-Funktion kann auch auf mehrdimensionale Arrays angewandt werden.

# In[16]:


#Eingänge: x1......xn
# Gewichte: w1.....wn
x = mp.array([3])
w = mp.array([4])
print(mp.dot(x,w))

x = mp.array([3, -2])
w = mp.array([-4, 1])
print(mp.dot(x,w))

