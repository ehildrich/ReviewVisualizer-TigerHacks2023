#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import calculator


# In[5]:


pip install -U selenium


# In[18]:


import scraper


# In[19]:


reviews = scraper.critic_responses


# In[20]:


review_words = calculator.createWordList(reviews, calculator.getWordsToRemove("Five Nights at Freddy's"))


# In[21]:


review_words


# In[22]:


review_words_df = pd.DataFrame(review_words, columns = ['Word'])


# In[23]:


review_words_df.head()


# In[24]:


word_counts = review_words_df.groupby(['Word'])


# In[25]:


plt.figure(figsize=(15, 10))
word_counts.size().sort_values(ascending=False).head(15).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Words Used in Movie Reviews")
plt.ylabel("Frequency of Words")


# In[ ]:




