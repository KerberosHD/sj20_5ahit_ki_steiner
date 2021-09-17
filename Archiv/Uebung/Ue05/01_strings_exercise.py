#!/usr/bin/env python
# coding: utf-8

# # 1. Fill missing pieces
# Fill `____` pieces below to have correct values for `lower_cased`, `stripped` and `stripped_lower_case` variables.

# In[1]:


original = ' Python strings are COOL! '
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()


# Let's verify that the implementation is correct by running the cell below. `assert` will raise `AssertionError` if the statement is not true.  

# In[2]:


assert lower_cased == ' python strings are cool! '
assert stripped == 'Python strings are COOL!'
assert stripped_lower_cased == 'python strings are cool!'


# # 2. Prettify ugly string
# Use `str` methods to convert `ugly` to wanted `pretty`.

# In[4]:


ugly = ' tiTle of MY new Book\n\n'


# In[9]:


# Your implementation:
pretty = ugly.lower().title().strip()


# Let's make sure that it does what we want. `assert` raises [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError) if the statement is not `True`.

# In[10]:


print('pretty: {}'.format(pretty))
assert pretty == 'Title Of My New Book'


# # 3. Format string based on existing variables
# Create `sentence` by using `verb`, `language`, and `punctuation` and any other strings you may need.

# In[11]:


verb = 'is'
language = 'Python'
punctuation = '!'


# In[16]:


# Your implementation:
secVerb = 'Learning '
adj = ' fun'
space = ' '
sentence = secVerb + language +space+ verb + adj + punctuation


# In[17]:


print('sentence: {}'.format(sentence))
assert sentence == 'Learning Python is fun!'

