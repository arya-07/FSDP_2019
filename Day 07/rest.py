# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:11:17 2019

@author: Hp
"""

import json
import requests

Host = "http://13.127.155.43/api_v0.1/sending"

data = {"First_name":"Arya","Last_name":"Sinha","Phone_Number":"7979934837"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )
def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving/get?=Phone_Number")
    return response

print (get_method().text)+

