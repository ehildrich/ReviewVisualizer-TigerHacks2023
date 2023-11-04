from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# initial conditions for selenium to simulate the next button
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options)

# TODO
# need to add functionalitiy to get the url from search tool instead of 
# directly pasting the url

url = "https://www.rottentomatoes.com/m/five_nights_at_freddys/reviews"

driver.get(url)

# get element with classname next
next_btn = driver.find_element(By.CLASS_NAME, "next") 

# response array
critic_responses = []

for i in range(0,100):
    
    # get the page source from selenium
    page = driver.page_source
    parsedText = BeautifulSoup(page, "html.parser")
    review_div = parsedText.findAll("p", class_="review-text")
    
    # store all the responses in an array
    for review_text in review_div:
            critic_responses.append(review_text.text)
    try: 
        next_btn.click()
    except:
        break

# close the selenium driver
driver.close()
