# -*- coding: utf-8 -*-
"""
Get djidf

@author: Xinyu Li
"""

import requests
import re
import pandas as pd

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*)<\/a>.*<span.*">(.*)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append({'code': item[0], 'name': item[1], 'price': float(item[2])})
    return dji_list

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
print(djidf)