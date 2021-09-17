#!/usr/bin/env python
# coding: utf-8

# # UE02 Python Einführung - Aufgaben 
# Arbeiten Sie nachfolgenden Aufgabenstellungen durch. 
# 
# >**Hinweis:** Abzugeben ist ein Python-File (Export siehe Menüeintrag `File > Download as`).

# ## Task 2.1.1 - Strings
# Beantworten Sie nachfolgende Frage bzw. schreiben Sie jenen Code, den es zur Erfüllung der jeweiligen Aufgabenstellung braucht:
# 1. Macht es einen Unterschied, ob man einfache oder doppelte Anführungsstriche verwendet? 
# 2. Erzeugen Sie mit <code>print(...)</code> folgende Ausgabe : **"Now, I'm able to use single quotes!"**
# 3. Geben Sie durch Verwendung von <code>x</code> und <code>y</code> die Zeichenkette **Hello, world!** mit <code>print(...)</code> aus.

# Antwort zu 1.: Es macht keinen Unterschied, nur wenn man innerhalbdes strings einfache verwendet muss man ausßerhalb doppelte Anführungsstriche verwenden

# In[4]:


#2.
print("Now, I'm able to use single quotes!")


# In[5]:


#3.
x, y = "Hello", "World"
print("%s, %s" %(x,y))


# ## Task 2.1.2 - Indexbasierte String-Manipulation
# Nehmen Sie vorher https://docs.python.org/3.8/tutorial/introduction.html#strings durch, und zwar ab der Textstelle "*Strings can be indexed...*" Als Bearbeitungsgrundlage dient <code>show</code>:
# 1. Geben Sie den zweiten Buchstaben der Zeichenkette aus
# 2. Geben Sie das Wort **eating** aus
# 3. Geben Sie alles nach **Software** aus
# 4. Geben Sie alles vor **the** aus
# 5. Geben Sie die letzten 3 Buchstaben der Zeichenkette aus

# In[2]:


show = "Software is eating the world!"
print(show[1])
print(show[12:18])
print(show[8:])
print(show[0:-10])
print(show[-4:-1])


# ## Task 2.1.3 - if, elif, else Statements
# 
# Es gilt:
# - Wenn <code>x</code> 'true' ist, hat die Ausgabe '**x was True!**' zu erfolgen
# - sonst **'x was False!'**

# In[23]:


x = False
if(x == True):
    print("x was True!")
else:
    print("x was False!")


# ## Task 2.2.4 - if, elif, else Statements
# 
# Es gilt:
# - Wenn <code>person</code> 'Georg' ist, hat die Ausgabe '**Welcome Georg**' zu erfolgen.
# - Ist <code>person</code> 'Jimmy', dann '**Welcome Jimmy**'.
# - Sonst '**Welcome, what is your name?**'

# In[27]:


person = 'Georg'
if(person == "Georg"):
    print("Welcome Georg")
elif(person == "Jimmy"):
    print("Welcome Jimmy")
else:
    print("Welcome, what is your name?")
    


# ## Task 2.2.5 - Loops, Lists, Dicts etc. 

# Iterieren Sie über die Liste <code>list1</code> und fügen Sie hierbei alle geraden Einträge der neu zu erstellenden Liste <code>even</code> und alle ungeraden der Liste <code>odd</code> hinzu. Setzen Sie den Modulo-Operator ein.

# In[4]:


list1 = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
# for number in list1:
#    if(number%2 == 0):
#        even.append(number)
#    else:
#        odd.append(number)
for number in list1:
    if(number%2):
       odd.append(number)
    else: 
        even.append(number)


# ## Task 2.2.6 - Loops, Lists, Dicts etc. 
# Geben Sie die *Keys* als auch die *Values* des Dictionaries <code>d1</code> aus.

# In[31]:


d1 = {'k1':1,'k2':2,'k3':3}
for key, value in d1.items():
    print(key,':' ,value)


# ## Task 2.2.7 - Loops, Lists, Dicts etc. 
# Erstellen ein Dictionary mit ein paar Namenseinträgen. Erstellen Sie in Folge ein zweites Dictionary mit weiteren Namenseinträgen. Fügen Sie beide Dictionaries zusammen und stellen Sie hierbei sicher, dass im "neuen" Dictionary keine Duplikate vorhanden sind. (Anm.: Testszenario mit mind. einer Namensgleichheit. Die Überprüfung hat manuell zu erfolgen).

# In[3]:


n1, n2= {1 : 'Markus', 2 : 'Julian', 3 : 'Tanja'}, {4 : 'Phillip', 5 : 'Julian', 6 : 'Guenther'}
test = 0
for name2 in n2:
    test= 0
    for name1 in n1:
        if n2[name2] == n1[name1]:
            test =1
    if test == 0:
            n1.update({name2:n2[name2]})
            
print(n1)


# ## Task 2.2.8
# Erstellen Sie mithilfe der *Built-in Function* `range` eine Liste mit Werten, die folgende Werte enthält: `[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. Details bzgl. Verwendung von `range` liefert diese [Quelle](https://docs.python.org/3.8/library/functions.html).

# In[2]:


list = [*range(0,101, 10)]
list = list (range(0,101, 10))

#list =[]
#for i in range(0,101, 10):
#    list.append(i)
print(list)


# In[4]:


name = "Homer"
print(f"His name is {name} ")

