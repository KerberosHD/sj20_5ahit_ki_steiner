#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2 as pypdf
import urllib.request as urllib2
from bs4 import BeautifulSoup


# In[2]:


get_ipython().system('pip install PyPDF2')


# In[ ]:





# # 2.1
# 

# In[3]:


list = []

with open('schachnovelletext13.pdf', 'rb') as pdf:
    reader = pypdf.PdfFileReader(pdf)
    print(reader.getDocumentInfo())
    #getDocumentInfo().producer
    


# In[ ]:





# # 2.2

# In[4]:


list = []

with open('schachnovelletext13.pdf', 'rb') as pdf:
    reader = pypdf.PdfFileReader(pdf)
    print(reader.getDocumentInfo())
    page = reader.getPage(0)
    print(page.extractText())
    for page in reader.pages:
        print(page.extractText())
    for page in reader.pages:
        list.append(page)


# In[5]:


for t in list:
    print(t.extractText())


# # 2.3
# 

# In[6]:


response = urllib2.urlopen('https://www.htlkrems.ac.at')
html_doc = response.read()


# In[7]:


soup = BeautifulSoup(html_doc, 'html.parser')


# In[8]:


strhtm = soup.prettify()


# In[9]:


print (strhtm[:100])


# In[10]:


soup.find_all('a')


# In[11]:


for link in soup.find_all('a'):
    print(link.get('href'))

