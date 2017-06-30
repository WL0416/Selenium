#!/usr/bin/python
import random
from faker import Factory

fake = Factory.create('en_AU')

def registerPage():
    registerData = []
    firstname = fake.first_name()
    registerData.append(firstname)
    print 'First Name: '+firstname
    lastname = fake.last_name()
    registerData.append(lastname)
    print 'Last Name:'+lastname
    phone = fake.phone_number()
    registerData.append(phone)
    print 'Phone Num.: '+phone
    email = fake.email()
    registerData.append(email)
    print 'Email: '+email

    address = fake.street_address()
    print address
    for _ in range(0,2):
        address = fake.address()
        address = address.split(',')
        address = address[0]
        address = address.split('\n')
        if len(address) == 3:
            address[0]=address[0]+address[1]
        registerData.append(address[0])
        print 'Address: '+address[0]

    city = fake.city()
    registerData.append(city)
    print 'City: '+city
    state = fake.state()
    registerData.append(state)
    print 'State: '+state
    postcode = fake.postcode()
    registerData.append(postcode)
    print 'Postal Code: '+postcode
    country = random.randint(1, 265)
    registerData.append(country)
    print 'Country: '+str(country)
    profile = fake.simple_profile()
    registerData.append(profile['username'])
    print 'Username: '+profile['username']
    password = fake.password()
    registerData.append(password)
    print 'Password: '+password
    registerData.append(password)
    print 'Confirm Password: '+password
    c = fake.country()

    print registerData

registerPage()