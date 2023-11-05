#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import calculator

def review_visuals(reviews, movie_title):
    #list of all significant words in all reviews
    review_words = calculator.createWordList(reviews, calculator.getWordsToRemove(movie_title))

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
    wc.to_file("wordcloud.png")

    # Create the graph
    colors = ["lightgreen", "green", "teal", "lightblue", "blue"]
    plt.figure(figsize=(15, 10))
    plt.axis("on")
    word_counts.size().sort_values(ascending=False).head(15).plot.bar(color=colors)
    plt.rc("xtick", labelsize=20)
    plt.xticks(rotation=50, fontsize="x-large")
    plt.xlabel("Words Used in Movie Reviews", fontsize="x-large")
    plt.ylabel("Frequency of Words", fontsize="x-large")

    # Display the graph
    plt.savefig("review_bar_graph.png", bbox_inches="tight")



