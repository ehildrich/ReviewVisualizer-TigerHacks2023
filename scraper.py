from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO
# make this beautiful

# initial conditions for selenium to simulate the next button
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options)

def generate_search_url(search_text):
    # i don't know what the technical term for this is
    plus_text = search_text.replace(" ", "+")
    return f"https://www.rottentomatoes.com/search?search={plus_text}"

# generate a movie url
# the easy way, but can't guarantee results
# example: "The Matrix" is only "matrix" in rotten tomatoes so can't give results
def get_movie_review_url(movie_name):
    lower_name = movie_name.lower()
    formatted_text = lower_name.replace(" ", "_").replace("'","")
    url = f"https://www.rottentomatoes.com/m/{formatted_text}/reviews"
    print(type(url))
    return url

# the selenium way so uses rotten tomato's search engine
# lots of breaking point
# if the website is updated the code needs to get updated
def get_movie_review_url_search(search_url):
    search_results_page = driver.get(search_url)

    movies_tab_select = driver.find_element(By.XPATH, "//*[@id='search-results']/nav/ul/li[3]")
    movies_tab_select.click()

    first_result = driver.find_element(By.XPATH, "//*[@id='search-results']/search-page-result[2]/ul/search-page-media-row/a[2]")
    movie_url = first_result.get_attribute('href')

    return f"{movie_url}/reviews"

# search text 
url = get_movie_review_url_search(generate_search_url('life of brian'))

driver.get(url)

# get next button
next_btn = driver.find_element(By.XPATH, "//*[@id='reviews']/div[1]/rt-button[2]") 

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

print(critic_responses)
