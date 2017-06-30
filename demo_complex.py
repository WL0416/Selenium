#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # allows you to enter Return key etc.
from selenium.webdriver.support.select import Select
from faker import Factory
import random
import time

fake = Factory.create('en_AU')
#driver = webdriver.Chrome('E:/RMIT/Semester 2/Software Testing/chromedriver')
driver=webdriver.Firefox()

def generateData():
    registerData = []
    firstname = fake.first_name()
    registerData.append(firstname)
    lastname = fake.last_name()
    registerData.append(lastname)
    phones = fake.phone_number()
    registerData.append(phones)
    emails = fake.email()
    registerData.append(emails)
    address1 = fake.address()
    address = address1.split('\n')
    registerData.append(address[0])
    registerData.append(address[1])
    citys = fake.city()
    registerData.append(citys)
    states = fake.state()
    registerData.append(states)
    postcodes = fake.postcode()
    registerData.append(postcodes)
    cData = fake.country()
    countryData = cData.upper()
    registerData.append(countryData)
    prof = fake.simple_profile()
    registerData.append(prof['username'])
    pw = fake.password()
    registerData.append(pw)
    registerData.append(pw)
    return registerData

def processRegister():
    driver.get('http://newtours.demoaut.com')
    field = driver.find_element_by_link_text('REGISTER')
    field.click()

    text = ['firstName','lastName','phone','userName','address1','address2','city','state','postalCode','country','email','password','confirmPassword']
    rdata = generateData()
    index = 0
    for content in text:
		print content
		check = driver.find_element_by_name(content)
		if content=='country':
			Select(check).select_by_visible_text(rdata[index])
		else:
			check.send_keys(rdata[index])
		index+=1
		#time.sleep(1)
    fieldend = driver.find_element_by_name('register')
    fieldend.click()
    driver.close()

processRegister()