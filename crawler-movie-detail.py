from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as BS
import csv
import pandas as pd
import io

file_name1 = 'raw-data.csv'
writer = csv.writer(io.open(file_name1, 'w', encoding='utf-8'))

pages = ['', '/101', '/201', '/301', '/401', '/501', '/601', '/701', '/801', '/901',
        '/1001', '/1101', '/1201', '/1301', '/1401', '/1501', '/1601', '/1701', '/1801', '/1901',
        '/2001', '/2101', '/2201', '/2301', '/2401', '/2501', '/2601', '/2701', '/2801', '/2901',
        '/3001', '/3101', '/3201', '/3301', '/3401', '/3501', '/3601', '/3701', '/3801', '/3901',
        '/4001', '/4101', '/4201', '/4301', '/4401', '/4501', '/4601', '/4701', '/4801', '/4901',
        '/5001', '/5101', '/5201', '/5301', '/5401', '/5501', '/5601', '/5701', '/5801', '/5901',
        '/6001', '/6101', '/6201']

class craigslist_crawler(object):
    def __init__(self):
        self.url = "https://www.the-numbers.com"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def write_header(self):
        writer.writerow(['', 'ReleaseDate', 'Movie', 'RunningTime', 'Source', 'Genre',
                        'ProductionMethod', 'CreativeType', 'ProductionCompanies',
                        'ProductionCountries', 'Languages', 'ProductionBudget',
                        'DomesticGross', 'WorldwideGross'])

    def write_body(self, page):
        driver = self.driver
        url = self.url + '/movie/budgets/all' + page
        driver.get(url)

        html = driver.page_source
        soup = BS(html, 'html.parser')

        for tr in soup.find_all('tr'):
            data = []
            for td in tr.find_all('td'):
                data.append(td.text.strip().replace('$','').replace(',',''))
                a = td.select_one('b > a')
                if a:
                    detail_url = a['href']
                    detail_crawler = craigslist_crawler()
                    detail_crawler.url = detail_crawler.url + detail_url
                    detail_crawler.driver.get(detail_crawler.url)

                    detail_html = detail_crawler.driver.page_source
                    detail_soup = BS(detail_html, 'html.parser')
                    h2 = detail_soup.body.find('h2', text='Movie Details')
                    if h2:
                        table = h2.find_next_sibling()

                        running_time = table.find('td', text='Running Time:')
                        if running_time:
                            running_time = running_time.find_next_sibling().text
                            data.append(running_time.strip())
                        else:
                            data.append('')

                        source = table.find('td', text='Source:')
                        if source:
                            source = source.find_next_sibling().text
                            data.append(source.strip())
                        else:
                            data.append('')

                        genre = table.find('td', text='Genre:')
                        if genre:
                            genre = genre.find_next_sibling().text
                            data.append(genre.strip())
                        else:
                            data.append('')

                        production_method = table.find('td', text='Production Method:')
                        if production_method:
                            production_method = production_method.find_next_sibling().text
                            data.append(production_method.strip())
                        else:
                            data.append('')

                        creative_type = table.find('td', text='Creative Type:')
                        if creative_type:
                            creative_type = creative_type.find_next_sibling().text
                            data.append(creative_type.strip())
                        else:
                            data.append('')

                        production_companies = table.find('td', text='Production/Financing Companies:')
                        if production_companies:
                            production_companies = production_companies.find_next_sibling().text
                            data.append(production_companies.strip())
                        else:
                            data.append('')

                        production_countries = table.find('td', text='Production Countries:')
                        if production_countries:
                            production_countries = production_countries.find_next_sibling().text
                            data.append(production_countries.strip())
                        else:
                            data.append('')

                        languages = table.find('td', text='Languages:')
                        if languages:
                            languages = languages.find_next_sibling().text
                            data.append(languages.strip())
                        else:
                            data.append('')
                    detail_crawler.driver.close()
            if(data):
                print("Inserting row: {}".format(','.join(data)))
                writer.writerow(data)

        driver.close()


crawler = craigslist_crawler()
crawler.write_header()

for page in pages:
    crawler = craigslist_crawler()
    crawler.write_body(page)

