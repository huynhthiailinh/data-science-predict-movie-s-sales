from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as BS
import csv
import pandas as pd
import io

file_name1 = 'raw-data1.csv'
writer = csv.writer(io.open(file_name1, 'w', encoding='utf-8'))

pages = ['', '101', '201', '301', '401', '501', '601', '701', '801', '901', 
        '1001', '1101', '1201', '1301', '1401', '1501', '1601', '1701', '1801', '1901',
        '2001', '2101', '2201', '2301', '2401', '2501', '2601', '2701', '2801', '2901',
        '3001', '3101', '3201', '3301', '3401', '3501', '3601', '3701', '3801', '3901',
        '4001', '4101', '4201', '4301', '4401', '4501', '4601', '4701', '4801', '4901',
        '5001', '5101', '5201', '5301', '5401', '5501', '5601', '5701', '5801', '5901',
        '6001', '6101', '6201']

class craigslist_crawler(object):
    def __init__(self, page):
        self.url = "https://www.the-numbers.com/movie/budgets/all/" + page
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def load_page(self):
        driver = self.driver
        driver.get(self.url)

        html = driver.page_source
        soup = BS(html, 'html.parser')

        for tr in soup.find_all('tr'):
            data = []

            # execute only once
            # for th in tr.find_all('th'):
            #     data.append(th.text)
            # if(data):
            #     print("Inserting header: {}".format(','.join(data)))
            #     writer.writerow(data)
            #     continue

            for td in tr.find_all('td'):
                data.append(td.text.strip().replace('$','').replace(',',''))
            if(data):
                print("Inserting row: {}".format(','.join(data)))
                writer.writerow(data)
        driver.close()


for page in pages:
    crawler = craigslist_crawler(page)
    crawler.load_page()

# delete empty rows
file_name2 = 'raw-data.csv'
df = pd.read_csv(file_name1, encoding='unicode_escape')
mdf = df.dropna()
mdf.to_csv(file_name2, index=False)