from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as BS
import csv
import pandas as pd

file_name1 = 'raw-data1.csv'

class craigslist_crawler(object):
    def __init__(self):
        self.url = "https://www.the-numbers.com/movie/budgets/all"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def load_page(self):
        driver = self.driver
        driver.get(self.url)

        html = driver.page_source
        soup = BS(html, 'html.parser')

        writer = csv.writer(open(file_name1, 'w'))

        for tr in soup.find_all('tr'):
            data = []

            # execute only once
            for th in tr.find_all('th'):
                data.append(th.text)
            if(data):
                print("Inserting header: {}".format(','.join(data)))
                writer.writerow(data)
                continue

            for td in tr.find_all('td'):
                data.append(td.text.strip().replace('$','').replace(',',''))
            if(data):
                print("Inserting row: {}".format(','.join(data)))
                writer.writerow(data)
        driver.close()

crawler = craigslist_crawler()
crawler.load_page()

# delete empty rows
file_name2 = 'raw-data.csv'
df = pd.read_csv(file_name1, encoding='unicode_escape')
mdf = df.dropna()
mdf.to_csv(file_name2, index=False)