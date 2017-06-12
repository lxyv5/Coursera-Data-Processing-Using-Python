# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:23:44 2017

@author: Xinyu Li
"""

import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('KO', start, today)
fields = ['date','open','close','high','low','volume']
list1 = []
for i in range(0,len(quotes)):
x = date.fromordinal(int(quotes[i][0]))
y = datetime.strftime(x,'%Y-%m-%d')
list1.append(y)
#print list1
quoteskodf = pd.DataFrame(quotes, index = list1, columns = fields)
quoteskodf = quoteskodf.drop(['date'], axis = 1)
#print quotesdf
listtemp = []
for i in range(0,len(quoteskodf)):
temp = time.strptime(quoteskodf.index[i],"%Y-%m-%d")
listtemp.append(temp.tm_mon)
print listtemp
tempkodf = quoteskodf.copy()
tempkodf['month'] = listtemp
closeMeansKO = tempkodf.groupby('month').mean().close
listKO = []
for i in range(1,13):
listKO.append(closeMeansKO[i])
listKOIndex = closeMeansKO.index
plt.plot(listKOIndex,listKO,'g*')
plt.show()