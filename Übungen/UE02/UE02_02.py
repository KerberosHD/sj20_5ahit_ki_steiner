#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


p = re.compile("5")
print(p.findall("Für 5 Semmeln habe ich 3.90 bezahlt"))


# In[3]:


p = re.compile("[1234567890]") #Sinn ist der gleiche
p = re.compile("[0-9]") #Sinn ist der gleiche
print(p.findall("Für 5 Semmeln habe ich 3.90 bezahlt"))


# In[4]:


p = re.compile(" [0-9] ")
print(p.findall("Für 5 Semmeln habe ich 3.90 bezahlt"))


# In[5]:


p = re.compile("[0-9]\.[0-9][0-9]")
print(p.findall("Für 5 Semmeln habe ich 3.90 bezahlt"))


# In[6]:


p = re.compile("[0-9]\.[0-9][0-9][€$]")
print(p.findall("Für 5 Semmeln habe ich 3.90$ bezahlt"))
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt"))


# In[7]:


p = re.compile(" [0-9] ")

print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50$ bezahlt."))


# In[8]:


#Es würde nicht funktionieren, weil man nur nach 3 Ziffern extrahiert


# In[9]:


p = re.compile("[0-9]+[.,][0-9][0-9][€$]?")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50 bezahlt."))


# In[10]:


p = re.compile("Telefonnummer")

print(p.search("Meine Telefonnummer ist 0664 555 0 123. Ruf schnell an!"))


# In[11]:


match = p.search("Meine Telefonnummer ist 0664 555 0 123. Ruf schnell an!")
print(match.span())
print(match.start())
print(match.end())


# In[12]:


#finditer: gibt ein object zurück, mit next(result) gibt man dann das match aus, welches als erstes matched
#match: mit match sucht man nach dem ersen zeichen eines wortes, wenn man aber z.B pattern = re.compile("o") hat und
#man mit pattern.match("dog") danach sucht, wird man nix finden, weil man mit pattern.match("dog", 1) suchen muss,
#weil man dann das zweite Zeichen eines wortes sucht. Standardgemäß sucht man immer das erste Zeichen


# In[13]:


print(re.search("Frau|Herr", "Sehr geehrter Frau Musterfrau! Ich darf sie darauf hinweisen, dass ..."))
print(re.search("Frau|Herr", "Sehr geehrter Herr Mustermann! Ich darf sie darauf hinweisen, dass ..."))


# In[14]:


re.findall(".und", "Der Hund hat keinen Mund ")


# In[15]:


someText = ["a", "abc", "bac"]

for text in someText:
    print(re.findall("^a", text))


# In[16]:


someText = ["a", "formula", "bac"]

for text in someText:
    print(re.findall("a$", text))


# In[17]:


re.findall("[^ ]", "Das ist ein Text mit Leerzeichen!")


# # 3.5 Re Tutorial

# In[18]:


import re


# In[19]:


pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful")


# In[20]:


string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)


# In[21]:


string = "Twelve:12 Eighty nine:89."
pattern = '\d+'

result = re.split(pattern, string)
print(result)


# In[22]:


string = 'Twelve:12 Eighty nine:89 Nine:9'
pattern = '\d+'

#maxsplit = 1
#split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)


# In[23]:


#multiline string
string = 'abc 12de 23 \n f45 6'

#matches all whitespace characters
pattern = '\s+'

#empty string

replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)


# In[24]:


#multiline string
string = 'abc 12de 23 \n f45 6'

#matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1)
print(new_string)


# In[25]:


string = 'abc 12de 23 \n f45 6'
#matches all whitespace characters
pattern = '\s+'

#empty string

replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)


# In[26]:


string = "Python is fun"

#check if 'Python is at the beginning'
match = re.search('\APython', string)

if match:
    print("pattern found inside of string")
else:
    print("not found")


# In[27]:


string = '39801 356, 2102 1111'

#Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
match = re.search(pattern, string)

if match:
    print(match.group())
else:
    print("pattern not found")

match.group(1)
match.group(2)
match.group(1, 2)
match.groups()
match.start()
match.end()
match.span()


# In[28]:


print(match.re)
match.string


# In[29]:


string = '\n and \r are escape sequences.'
result = re.findall(r'[\n\r]', string)
print(result)


# # 3.6 Mailadressen

# In[36]:


import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import csv


# In[32]:


# Website laden
response = urllib2.urlopen('https://www.htlkrems.ac.at')
html_doc = response.read()
# Das BeautifulSoup Object soup repräsentiert das „geparste“ HTML-Dokument
soup = BeautifulSoup(html_doc, 'html.parser')
# Das „geparste“ HTML-Dokument formatieren, sodass jeder Tag bzw. Textblock
# in einer separaten Zeile ausgegeben wird
strhtm = soup.prettify()
# Ein paar Zeilen ausgeben
print (strhtm[:1000]) 


# In[33]:


regex = re.compile("[a-z]+[@][a-z]+[.][a-z]+")
result = regex.findall(strhtm)
print(result)


# In[37]:


with open('regex.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(result)

