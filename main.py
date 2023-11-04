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


# exampleReviews = ["Overall, the film needed more of the tension the video game series is known for, not to mention their arcade-fun terror, but it still serves as a solid 1987 Five Nights at Freddy’s franchise opener.", "The pacing is bad, the plotting is both convoluted and also somehow weirdly shallow, the writing is laughable, and the action is simplistic. I would not recommend seeing Five Nights at Freddy’s, as it is not good.", "A rushed second half, struggling to explain certain character's storylines fails to make the film thrilling or fun. I would say watch Child's Play or MEGAN if you want to see a silly, but clever horror about products that shouldn't be coming to life."]
exampleReviews = scraper.critic_responses
title = "Five Nights at Freddy's"

wordsToRemove = getWordsToRemove(title)

wordList = createWordList(exampleReviews, wordsToRemove)
print(wordList)

input('Press ENTER to exit')
