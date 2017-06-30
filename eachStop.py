#!/usr/bin/python
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # allows you to enter Return key etc.

driver = webdriver.Chrome('E:/RMIT/Semester 2/Software Testing/chromedriver')
def processStation(station):

    driver.get('http://ptv.vic.gov.au')
    #time.sleep(1)
    field = driver.find_element_by_link_text('Next 5 departures')
    field.click()
    #time.sleep(1)
    field = driver.find_element_by_id('Form_ModeSearchForm_Search')
    field.send_keys(station)
    field1 = driver.find_element_by_id('Form_ModeSearchForm_action_doModeSearch')
    field1.click()
    invalid_station(station)
    valid_station(station)
    #driver.close()

# replace pass with your code here
def valid_station(station):
    continuelink = driver.find_element_by_partial_link_text(station)
    assert continuelink != None, 'invalid station'

def invalid_station(station):
    assert 'Sorry, there were no results for your search.' not in driver.page_source, 'Showing an invalid message when I have a correct station'

first = True

for stationInfo in csv.reader(open('E:/RMIT/Semester 2/Software Testing/stops.txt')):
    if first:
        first = False
    else:
        station = stationInfo[1]
        print station
        processStation(station)
