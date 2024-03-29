#!/usr/bin/env python
# coding: utf-8

# # 1. Fill the missing pieces of the `count_even_numbers` function
# Fill `____` pieces of the `count_even_numbers` implemention in order to pass the assertions. You can assume that `numbers` argument is a list of integers.

# In[6]:


def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    numbers.append(num)
    return count


# In[7]:


assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4


# # 2. Searching for wanted people
# Implement `find_wanted_people` function which takes a list of names (strings) as argument. The function should return a list of names which are present both in `WANTED_PEOPLE` and in the name list given as argument to the function.

# In[8]:


WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']


# In[9]:


# Your implementation here
def find_wanted_people(people):
    found_people = []
    for p1 in WANTED_PEOPLE:
        for p2 in people:
            if p1 == p2:
                found_people.append(p2)
    return found_people


# In[10]:


people_to_check1 = ['Donald Duck', 'Clint Eastwood', 'John Doe', 'Barack Obama']
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert 'John Doe' in wanted1
assert 'Clint Eastwood'in wanted1

people_to_check2 = ['Donald Duck', 'Mickey Mouse', 'Zorro', 'Superman', 'Robin Hood']
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []


# # 3. Counting average length of words in a sentence
# Create a function `average_length_of_words` which takes a string as an argument and returns the average length of the words in the string. You can assume that there is a single space between each word and that the input does not have punctuation. The result should be rounded to one decimal place (hint: see [`round`](https://docs.python.org/3/library/functions.html#round)).

# In[15]:


# Your implementation here
def average_length_of_words (word):
    sumwords =''
    wordlist =[]
    wordlist = word.split(' ')
    for w in wordlist:
        sumwords += w
    average = len(sumwords) / len(wordlist)
    return  round(average, 1)


# In[16]:


assert average_length_of_words('only four lett erwo rdss') == 4
assert average_length_of_words('one two three') == 3.7
assert average_length_of_words('one two three four') == 3.8
assert average_length_of_words('') == 0

