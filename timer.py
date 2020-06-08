# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:41:13 2020

@author: felip
"""

import os # For screen clear command
import time # For timer

minute = int(input('Enter any amount of minutes you want -+==> '))
second = int(input('Enter any amount of seconds you want -+==> '))
timer =  minute*3600 + second*60
print('{}:{}'.format(minute,second))
while time > 0:
   os.system("cls") # Replace "{}" as "CLS" for windows or "CLEAR" for other.
   time = time - 1
   seconds = (time // 60) % 60
   minutes = (time // 3600)
   print('Time Left -+==> ',minutes,':',seconds,)
if time == 0:
   os.system("cls") # Replace "{}" as "CLS" for windows or "CLEAR" for other. 
   print('Time Is Over!')