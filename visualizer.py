#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import calculator
import scraper

# First get the reviews
reviews = scraper.critic_responses

# Then create a list of words used in those reviews, excluding filler words
review_words = calculator.createWordList(reviews, calculator.getWordsToRemove("Five Nights at Freddy's"))


review_words_df = pd.DataFrame(review_words, columns = ['Word'])
word_counts = review_words_df.groupby(['Word'])

# Create the graph
plt.figure(figsize=(15, 10))
word_counts.size().sort_values(ascending=False).head(15).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Words Used in Movie Reviews")
plt.ylabel("Frequency of Words")

# Display the graph
plt.show()
