#!/usr/bin/python 
# Usage: ./banana.py <start_date> <days>
# Author: David Byrne
# Description:Using a cost map returns the cost based on current date and days after.  
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date

#Pre-Define a data structure to store the static cost for each day of the year  
#NOTE I ommited the condition for leap year, worst case we over budget for one day every fourth year..
class bannanna_cost_map :  
 def __init__(self): 
   self.cost = dict()
   for i in range(1,13): 
     if i in [4,6,9,11]: days = 30 
     elif (i == 2): days = 29 
     else: days = 31
     daily_cost = dict()
     for day in range(1,days+1):
       if (day > 0 and day < 8): 
         daily_cost[day]=float('.05')
       elif  (day > 7 and day < 15):
         daily_cost[day]=float('.10')
       elif (day > 14 and day < 22):
         daily_cost[day]=float('.15')
       elif  (day > 21 and day < 29):
         daily_cost[day]=float('.20')
       elif (day > 28): 
         daily_cost[day]=float('.25')
       else : 
         print("Bad input. Got day of",day)
         exit()
     self.cost[i]=daily_cost
     print(daily_cost.items())





def cost_of_bananas(date_str,days):
  my_date=datetime.strptime(date_str,'%m/%d/%Y')
  day=my_date.day
  month=my_date.month
  price_map = bannanna_cost_map()
  
  total_cost=float(0)
  for i in range(1,days+1):
    day=my_date.day 
    month=my_date.month
    if not my_date.weekday() in [5,6] : 
      total_cost=total_cost+float(price_map.cost[month][day])
      print("Date: ",my_date," ",my_date.strftime('%A')," Adding",price_map.cost[month][day])    
    my_date=my_date+timedelta(days=1)  
  
  return("{0:.2f}".format(total_cost))
  

## ENTRY POINT 

date = sys.argv[1]
days = int(sys.argv[2])
print("Total budget needed :",cost_of_bananas(date,days))

