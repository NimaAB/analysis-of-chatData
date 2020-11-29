import os
import numpy as np
import math
import json 
from datetime import datetime

with open('./data/message_1.json') as json_file:
    data = json.load(json_file)

date = []

for el in data['messages']:
    if el['sender_name'] == "xx yy":
        intFormat = int(el['timestamp_ms'])
        #conv = datetime.datetime.fromtimestamp(intFormat)
        #date.append(conv.strftime('%Y-%m-%d %H:%M:%S'))
        date.append(intFormat)

#converting timestamps to day-month-year and hour:minute formar

for i in date:
    #dt_obj = datetime.fromtimestamp(i,tz=None).strftime('%d-%m-%Y') 
    print(np.datetime(i))


timestamp = 1553367060


#then counting stamps which has equal day and month and year:
#then saving the counts in a vektor with a respective date:
# 
# ploting number of messages per day:
