# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:20:24 2019

@author: Hp
"""
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)

response = requests.get(url)
response.content
jsondata = response.json()
jsondata["coord"]
jsondata["weather"]
jsondata["wind"]["speed"]
jsondata["sys"]["sunrise"]
jsondata["sys"]["sunset"]