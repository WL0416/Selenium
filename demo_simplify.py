#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # allows you to enter Return key etc.
from selenium.webdriver.support.select import Select
from faker import Factory
import random
import time

fake = Factory.create('en_AU')
driver = webdriver.Chrome('E:/RMIT/Semester 2/Software Testing/chromedriver')

driver.get('http://newtours.demoaut.com')

field = driver.find_element_by_link_text('REGISTER')
field.click()

firstname = fake.first_name()
lastname = fake.last_name()
phones = fake.phone_number()
emails = fake.email()
address1 = fake.address()
address = address1.split('\n')
citys = fake.city()
states = fake.state()
country = random.randint(1,266)
prof = fake.simple_profile()
pw = fake.password()
postcodes = fake.postcode()

field0 = driver.find_element_by_name('firstName')
field0.send_keys(firstname)
print 'firstName'
time.sleep(1)
field1 = driver.find_element_by_name('lastName')
field1.send_keys(lastname)
print 'lastname'
time.sleep(1)
field2 = driver.find_element_by_name('phone')
field2.send_keys(phones)
print 'phone'
time.sleep(1)
field3 = driver.find_element_by_id('userName')
field3.send_keys(emails)
print 'email'
time.sleep(1)
field12 = driver.find_element_by_name('address1')
field12.send_keys(address[0])
print 'address1'
time.sleep(1)
field13 = driver.find_element_by_name('address2')
field13.send_keys(address[1])
print 'address2'
time.sleep(1)
field5 = driver.find_element_by_name('city')
field5.send_keys(citys)
print 'city'
time.sleep(1)
field6 = driver.find_element_by_name('state')
field6.send_keys(states)
print 'state'
time.sleep(1)
field7 = driver.find_element_by_name('postalCode')
field7.send_keys(postcodes)
print 'postcode'
time.sleep(1)
field8 = driver.find_element_by_name('country')
Select(field8).select_by_value(str(country))
print 'country'
time.sleep(1)
field9 = driver.find_element_by_name('email')
field9.send_keys(prof['username'])
print 'username'
time.sleep(1)
field10 = driver.find_element_by_name('password')
field10.send_keys(pw)
print 'pw1'
time.sleep(1)
field11 = driver.find_element_by_name('confirmPassword')
field11.send_keys(pw)
print 'pw2'
time.sleep(1)
field14 = driver.find_element_by_name('register')
field14.click()
driver.close()