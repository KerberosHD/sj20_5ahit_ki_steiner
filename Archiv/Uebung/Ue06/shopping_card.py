#!/usr/bin/env python
# coding: utf-8

# In[46]:


import os

path = "shopping_cart.txt"
path2 = "shopping_cart2.txt"

def create_file():
    with open(path, "w") as file:
        file.write('#Nr;Menge;Einzelpreis;Bezeichnung\n')

def add_product(nr, amount, price, description):
    with open(path, "a") as file:
        file.write("%s;%s;%s;%s\n" %(nr,amount,price,description))

def create_second_file():
    result=0
    count=0
    with open(path2, "w") as file2:
        with open(path, "r+") as file:
            for line in file:
                if (count == 0):
                    file2.write('#Nr;Gesamtpreis;Bezeichnung\n')
                    count = count + 1
                else:
                    values = line.split(';')
                    result = float(values[1]) * float(values[2])
                    file2.write("%s;%s;%s"%(values[0],result,values[3]))
                
def check_results():
    result_file1=0
    result_file2=0
    count=0
    with open(path, "r+") as file1:
            for line in file1:
                if (count == 0):
                    count += 1
                else:
                    values = line.split(';')
                    result_file1 += float(values[1]) * float(values[2])
    count=0
    with open(path2, "r+") as file2:
            for line in file2:
                if (count == 0):
                    count += 1 
                else:
                    values = line.split(';')
                    result_file2 += float(values[1])
    assert result_file1 == result_file2
    

create_file()
add_product('4714',2,100.20,'Riesenschultüte')
add_product('0815',10,2.33,'Kaugummi')
add_product('9222',5,18.50,'Maus')
add_product('4523',160,80,'Monitor')
add_product('4521',90,12,'Mouspad')
add_product('9040',0.5,90,'Zuckerl')
add_product('8505',11,45,'Tasche')
create_second_file()
check_results()


# In[ ]:




