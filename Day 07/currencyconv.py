# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:38:23 2019

@author: Hp
"""

#Currency Converter Convert  from USD to INRimport requests
import requests
Dollar=int(input("Enter the amount in dollar"))
url="https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=48d79e91a85296c5f743"
response = requests.get(url)
response.content
jsondata = response.json()
value=jsondata["USD_PHP"]
INR=value*Dollar
print("Amount in INR:" +str(INR))