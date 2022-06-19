from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craigslist_crawler(object):
    def __init__(self):
        self.url = "https://www.the-numbers.com/movie/budgets/all"
        self.driver = webdriver.Chrome("C://setup//chromedriver_win32//chromedriver.exe")
        
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_text_data = driver.find_elements_by_class_name("data")
        all_link_data = driver.find_elements(By.CSS_SELECTOR, "table a")
        all_data = []
        for i in range(0, len(all_text_data), 4):
            stt = all_text_data[i].text
            production_budget = all_text_data[i+1].text[2:]
            domestic_gross = all_text_data[i+2].text[2:]
            worldwide_gross = all_text_data[i+3].text[2:]
            all_data.append([stt, production_budget, domestic_gross, worldwide_gross])

        j = 0
        for i in range(0, len(all_link_data), 2):
            release_date = all_link_data[i].text
            movie = all_link_data[i+1].text
            all_data[j] += [release_date, movie]
            j+=1

        print('stt', 'release_date', 'movie', 'production_budget', 'domestic_gross', 'worldwide_gross')

        for i in all_data:
            stt = i[0]
            release_date = i[4]
            movie = i[5]
            production_budget = i[1]
            domestic_gross = i[2]
            worldwide_gross = i[3]
            print(stt, release_date, movie, production_budget, domestic_gross, worldwide_gross)

    def close_webdriver(self):
        self.driver.close()

crawler = craigslist_crawler()
crawler.load_page()
crawler.close_webdriver()


