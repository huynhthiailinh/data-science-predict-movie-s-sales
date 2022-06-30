from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
t = 625
for i in range(10):
    url = "https://www.booking.com/searchresults.vi.html?label=gen173nr-1DCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AED6AEBiAIBqAIDuAKBn9WVBsACAdICJDkyZjMzNDM5LWNjYjgtNDk0My04MDUwLTkyMzI2N2I5NjZjZNgCBOACAQ&sid=72bff0a7eb9e51985d80010fc4502590&aid=304142&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AED6AEBiAIBqAIDuAKBn9WVBsACAdICJDkyZjMzNDM5LWNjYjgtNDk0My04MDUwLTkyMzI2N2I5NjZjZNgCBOACAQ%26sid%3D72bff0a7eb9e51985d80010fc4502590%26sb_price_type%3Dtotal%26%26&ss=Ha%CC%80+N%C3%B4%CC%A3i&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&dest_id=-3714993&dest_type=city&checkin_year=2022&checkin_month=6&checkin_monthday=26&checkout_year=2022&checkout_month=6&checkout_monthday=27&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset="
    url = url + str(t)
    t = t + 25
    driver.get(url)
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    #all hotels in pagination = 1 
    hotels = page_source.select('.dd023375f5 .a4225678b2 > a')
    data_bookings = []
    for hotel in hotels: 
        link = hotel['href']
        driver.get(link)
        page_source = BeautifulSoup(driver.page_source,'html.parser')
        type_hotel = "apartment"
        locations = page_source.select('.hp_address_subtitle')
        try:
            location = locations[0].getText()
        except:
            location = ""
        ratings = page_source.select('.b5cd09854e.d10a6220b4')
        try:
            rating = ratings[0].getText()
        except: 
            rating = 0
        reviewers = page_source.select('.b5cd09854e.c90c0a70d3.db63693c62')
        try:
            reviewer = reviewers[0].getText()
        except: 
            reviewer = 0
        distances = page_source.select('#basiclayout > div.k2-property_page--layout.k2-hp_full-width--layout > div > div.bui-grid__column.bui-grid__column-12.js-k2-hp--block.k2-hp--location_surroundings > div > div.hp_location_block__content_container > div:nth-child(3) > ul > li:nth-child(9) > div > div.bui-list__item-action.hp_location_block__section_list_distance')
        try:
            distance = distances[0].getText() 
        except: 
            distance = 0
        rooms = page_source.select('.hprt-roomtype-link')
        areas = page_source.select('.hprt-facilities-block .bui-spacer--medium .hprt-facilities-facility:first-child')
        prices = page_source.select('.hprt-price-block .prco-valign-middle-helper')
        type_bed = page_source.select('.hprt-roomtype-bed .bed-types-wrapper .rt-bed-types li span:first-child')
        for i in range(len(rooms)): 
            type_bed = page_source.select('.hprt-roomtype-bed .bed-types-wrapper .rt-bed-types li span:first-child')
            try:
                type_bed =  type_bed[i].getText()
            except: 
                type_bed =  ""
            try:
                price = prices[i].getText()
            except: 
                price = 0
            try: 
                area = areas[i].getText()
            except: 
                area = 0
            data_room_row =  []
            data_room_row.append(type_hotel)
            data_room_row.append(location)
            data_room_row.append(rating)
            data_room_row.append(reviewer)
            data_room_row.append(distance)
            data_room_row.append(type_bed)
            data_room_row.append(area)
            data_room_row.append(price)
            data_bookings.append(data_room_row)
    
result = pd.DataFrame(data=data_bookings)
result.to_csv('rawdata.csv')
