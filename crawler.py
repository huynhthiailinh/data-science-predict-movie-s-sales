from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

df = []
page = 1

while page < 6300:
    url = "https://www.the-numbers.com/movie/budgets/all/" + str(page)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    html = driver.page_source
    df += pd.read_html(html)

    driver.close()
    page += 100

final_df = pd.concat([df[0],df[1],df[2],df[3],df[4],df[5],df[6],df[7],df[8],df[9],
    df[10],df[11],df[12],df[13],df[14],df[15],df[16],df[17],df[18],df[19],
    df[20],df[21],df[22],df[23],df[24],df[25],df[26],df[27],df[28],df[29],
    df[30],df[31],df[32],df[33],df[34],df[35],df[36],df[37],df[38],df[39],
    df[40],df[41],df[42],df[43],df[44],df[45],df[46],df[47],df[48],df[49],
    df[50],df[51],df[52],df[53],df[54],df[55],df[56],df[57],df[58],df[59],
    df[60],df[61],df[62]])

final_df.to_csv('raw-data.csv')