#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import calculator
import scraper


reviews = scraper.critic_responses

#list of all significant words in all reviews
review_words = calculator.createWordList(reviews, calculator.getWordsToRemove(""))

#put list into dataframe
review_words_df = pd.DataFrame(review_words, columns = ['Word'])
word_counts = review_words_df.groupby(['Word'])

#create word cloud object
wc = WordCloud(background_color="white", font_path="./arial.ttf")

#get text string to generate review word cloud
review_text = ""
for word in range(len(review_words)):
    review_text = review_text + (review_words[word]) + " "


#create and show word cloud
wc.generate(review_text)
plt.axis("off")
plt.imshow(wc)


# Create the graph
plt.figure(figsize=(15, 10))
plt.axis("on")
word_counts.size().sort_values(ascending=False).head(15).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Words Used in Movie Reviews")
plt.ylabel("Frequency of Words")

# Display the graph
plt.show()



