#!/usr/bin/python

import os
import time
import datetime

from Adafruit_8x8 import EightByEight

import NSEphem

try:
   grid = EightByEight(address=0x70)
except IOError:
   print "LED Grid not connected, exiting"
   exit()

def flash(r,c,cnt,t):
   if ( cnt*2 > t ):
      if (t % 2 == 0 ):
        grid.setPixel(r,7-c,1)
      else:
        grid.setPixel(r,7-c,0)
   else:
      grid.setPixel(r,7-c,0)

ticks = 0
day_done = -1

while (True): 

   # refresh strings every day at 8AM
   now = datetime.datetime.now()
   if ( day_done != now.day ):
      # print "day, hour, minute", now.day, now.hour, now.minute

      if ((now.hour == 8 and now.minute < 5) or (day_done == -1)):
         # print "getting new strings"
         All_NS_obj = NSEphem.CreateAllNightSkyStrings()
         all_NS_strings = All_NS_obj.get_all_NS_strings()
         day_done = now.day

   ticks = ticks +1
   if (ticks > 20): 
      ticks = 0
            
   for row, aNightSkyString in enumerate(all_NS_strings):      
           
      NS_object_string = aNightSkyString
            
      # test strings:

      #   Earth
      #if (row == 1):
      #   NS_object_string = "X18ccccccccZ"

      #   Sun
      #if (row == 2):
      #   NS_object_string = "X28ccaaaaaaZ"

      #   Moon
      #if (row == 3):
      #   NS_object_string = "X38cbaaaaaaZ"

      #   ISS
      #if (row == 4):
      #   NS_object_string = "X48aaajakaaa"

      #   Venus
      #if (row == 5):
      #   NS_object_string = "X58cccaaaaaZ"

      #   Mars
      #if (row == 6):
      #   NS_object_string = "X68abccccccZ"

      #   Jupiter
      #if (row == 7):
      #   NS_object_string = "X78aaaaaaabc"

      #   Saturn
      #if (row == 8):
      #   NS_object_string = "X88ccbaaaaaa"

      #print "row, string", row, NS_object_string
            
      for col in range (0,8):
         char = NS_object_string[col+3]
         if (char=='a'):
             grid.setPixel(row,7-col,0)
         if (char=='b'):
             grid.setPixel(row,7-col,1)
         if (char=='c'):
             grid.setPixel(row,7-col,1)
         if (char=='g'):
             flash(row,col,1,ticks)
         if (char=='h'):
             flash(row,col,2,ticks)
         if (char=='i'):
             flash(row,col,3,ticks)
         if (char=='j'):
             flash(row,col,4,ticks)
         if (char=='k'):
             flash(row,col,5,ticks)
         if (char=='l'):
             flash(row,col,6,ticks)

   time.sleep(0.1)


