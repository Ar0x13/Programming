#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Temlate recognizing programm by Andrey Ruban
#

import re
import pdb

# Variables initialization
next_round = "yes"
dictionary = {}
result = "No result"
pdb.set_trace()

# Business logic
try:
    # check for correct type of input data
    while next_round.lower() == "yes":
        templ_name = input('Enter template name: \n')
        sequence = input('Enter template data: \n')
        if templ_name == '' or sequence == '':
            print('Enter correct types of data...')
            continue
        dictionary[templ_name] = sequence

        next_round = input("Do you want to enter more templates?: yes or no \n")
        if next_round == "no":
            break

    # Print dictionary with data
    # print('Your temaplte name and temlate itself: ', dictionary)
    print('Values: ')
    values = list(dictionary.values())

    # Data for recognition
    pattern = input("Enter data to check in templates: \n")

    for i in values:

        print('Looking for "%s" in "%s" ->' % (pattern, i))
        for key, value in dictionary.items():
            print(key, value)
            print(re.search(pattern, i))
            if re.search(pattern, i):
                print(key)
                result = 'Its {} template'.format(k)
                break

except Exception as e:
    print(e)

finally:
    print(result)
