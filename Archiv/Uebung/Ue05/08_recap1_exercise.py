#!/usr/bin/env python
# coding: utf-8

# # 1. Super vowels
# Implement `super_vowels` function which takes a string as an argument and returns a modified version of that string. In the return value of `super_vowels`, all vowels should be in upper case whereas all consonants should be in lower case. The vowels are listed in the `VOWELS` variable.

# In[4]:


VOWELS = ['a', 'e', 'i', 'o', 'u']


# In[7]:


# Your implementation here
def super_vowels (text):
    char_list = list(text.lower())
    sentence = ''
    for char in char_list:
        if char in VOWELS:
            sentence += char.upper()
        else:
            sentence += char

    return sentence


# In[8]:


assert super_vowels('hi wassup!') == 'hI wAssUp!'
assert super_vowels('HOw aRE You?') == 'hOw ArE yOU?'


# # 2. Playing board
# Implement `get_playing_board` function which takes an integer as an argument. The function should return a string which resemples a playing board (e.g. a chess board). The board should contain as many rows and columns as requested by the interger argument. See the cell below for examples of desired behavior.
# 

# In[3]:


# Your implementation here
def get_playing_board (number):
    even = ''
    odd = ''
    count = 0
    while count < number:
        if count % 2 ==0:
           even += ' '
           odd += '*'

        else:
            even += '*'
            odd += ' '
        count += 1
     count = 0

        board = ''
    while count < number:
        if count % 2 == 0:
            board += even + '\ln'
        else:
            board += odd + '\ln'
        count += 1


# In[ ]:


board_of_5 = (
' * * \n'
'* * *\n'
' * * \n'
'* * *\n'
' * * \n'
)

board_of_10 = (
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
)

assert get_playing_board(5) == board_of_5
assert get_playing_board(10) == board_of_10

print(get_playing_board(50))

