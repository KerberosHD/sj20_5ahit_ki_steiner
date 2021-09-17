#!/usr/bin/env python
# coding: utf-8

# In[26]:


import os

WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(os.path.dirname(WORKING_DIR), 'UE07')


# In[37]:


import sys

def calculate(input_file, output_file):
    try:
        writefile = open(output_file, 'w+')
        writefile.write('#Nr;Preis;Beschreibung\n')
        with open(input_file, 'r') as openfile:
            for line in openfile:
                if not line.startswith('#'):
                    val = line.split(';')
                    writefile.write(val[0] + ";" + str(round(float(val[1]) * float(val[2]),2)) + ";" + val[3])            
        writefile.close()
        
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an float.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise 


# In[38]:


calculate('shopping_cart.txt', 'shopping_cart2.txt')


# In[19]:


def check_overall_sum(input_file):
    sum_ = 0.0
    with open(input_file, 'r') as openfile:
        for line in openfile:
            if not line.startswith('#'):
                val = line.split(';')
    return sum_


# In[20]:


def read_file(input_file):
    arr = []
    with open(input_file, 'r') as openfile:
        arr = openfile
    return arr


# In[21]:


assert check_overall_sum('shopping_cart.txt') == check_overall_sum('shopping_cart.txt')

