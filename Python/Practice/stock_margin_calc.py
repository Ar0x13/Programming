#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Margin stock calculator.

author: Andrey Ruban
website: how2.pp.ua
last modified: Sep 2018

Every programm should has:
1 Check input data before business logic
2 Exception termination
3 Data output
"""

try:
    amount = float(input("Enter amount of cc: "))
    price_past = float(input("Enter past price: "))
    price_now = float(input("Enter price now: "))

    def logic():
        result = (amount * price_now ) - (amount * price_past)
        print("Your margin is: ", result)
        
    def run():
        logic()


except Exception as error:
	print(error)

finally:
    if __name__ == '__main__':
        run()
