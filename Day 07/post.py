# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:54:31 2019

@author: Hp
"""

import json
import requests

Host = "https://entvdbb2bs7yr.x.pipedream.net/"

data = {"firstname":"Arya","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )