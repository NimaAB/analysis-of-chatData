
import os
import math
import json 

with open('./data/message_1.json') as json_file:
    data = json.load(json_file)

for el in data['messages']:
    if el['sender_name'] == "xx yy":
        print(el['timestamp_ms'])

#converting timestamps to day-month-year and hour:minute formar
#then counting stamps which has equal day and month and year:
#then saving the counts in a vektor with a respective date:
# 
# ploting number of messages per day:  

