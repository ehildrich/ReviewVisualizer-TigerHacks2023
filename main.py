from calculator import getWordsToRemove
from calculator import createWordList
from scraper import Scraper


#TODO integrate this into a GUI
movie_name = input("Enter the movie name: ")

# setup the scraper

# get reviews from 10 pages
scraper = Scraper(movie_name, 10)
scraper.initialize_driver("--ignore-certificate-error", "--incognito", "--headless")
scraper.scrape()

reviews = scraper.critic_responses
title = scraper.movie_name 

wordsToRemove = getWordsToRemove(title)

wordList = createWordList(reviews, wordsToRemove)
print(wordList)

input('Press ENTER to exit')

