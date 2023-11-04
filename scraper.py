from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self, search_text, PAGINATION_RANGE = 100):

        # initial conditions for selenium to simulate the buttons
        self.options = webdriver.ChromeOptions() 

        # default conditions
        self.options.add_argument("--ignore-certificate-error")
        self.options.add_argument("--incognito")
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(self.options)

        self.url = ""
        self.search_text = search_text; 
        self.PAGINATION_RANGE = PAGINATION_RANGE 
        self.critic_responses = []
        self.movie_name = ""

    # initialize selenium
    def initialize_driver(self, *argv):
        for arg in argv:
            self.options.add_argument(arg)

        self.driver = webdriver.Chrome(self.options)

    def get_search_url(self, search_text):
        plus_text = search_text.replace(" ", "+")
        return f"https://www.rottentomatoes.com/search?search={plus_text}"

    def get_review_url(self, search_url):
        search_results_page = self.driver.get(search_url)

        # xpath is the way to access html elements using regular expressions  
        movies_tab_select = self.driver.find_element(By.XPATH, "//*[@id='search-results']/nav/ul/li[@data-filter='movie']")
        movies_tab_select.click()

        first_result = self.driver.find_element(By.XPATH, "//*[@id='search-results']/search-page-result[@type='movie']/ul/search-page-media-row[1]/a[@slot='title']")
        movie_url = first_result.get_attribute('href')

        return f"{movie_url}/reviews"
    
    def scrape(self):
        self.search_url = self.get_search_url(self.search_text)
        self.url = self.get_review_url(self.search_url) 

        # use the driver to get the website
        self.driver.get(self.url)

        # get next button
        next_btn = self.driver.find_element(By.XPATH, "//*[@id='reviews']/div[1]/rt-button[2]") 

        # get the movie name
        page = self.driver.page_source
        parsedText = BeautifulSoup(page, "html.parser")
        self.movie_name = parsedText.find("a", class_="sidebar-title").text 

        for i in range(0,self.PAGINATION_RANGE):
            
            # get the page source from selenium
            page = self.driver.page_source
            parsedText = BeautifulSoup(page, "html.parser")

            # the reviews are <p> inside html <div> with classname "review-text" 
            review_div = parsedText.findAll("p", class_="review-text")
            
            # store all the responses in an array
            for review_text in review_div:
                    self.critic_responses.append(review_text.text)
            try: 
                next_btn.click()
            except:
                break

        # close the selenium driver
        self.driver.close()

# example use 
#    scraper = Scraper("dark night rises", 10) # pulls reviews from 10 pages
#    scraper.initialize_driver("--ignore-certificate-error", "--incognito", "--headless")
#    scraper.scrape()
#
#    # uncomment the following line to display the responses
#    print(scraper.critic_responses)
