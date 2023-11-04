#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import calculator
import scraper


reviews = scraper.critic_responses
review_words = calculator.createWordList(reviews, calculator.getWordsToRemove(""))

review_words_df = pd.DataFrame(review_words, columns = ['Word'])

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
wc = WordCloud(background_color="white", font_path="./arial.ttf")

review_text = ""
for word in range(len(review_words)):
    review_text = review_text + (review_words[word]) + " "

wc.generate(review_text)

plt.axis("off")
plt.imshow(wc)





