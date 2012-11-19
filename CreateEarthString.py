import sys
import datetime
import time
import urllib2

'''
Created on Nov 15, 2012

@author: tnielsen
'''
class CleardarkskyEarth:

    """Scrapes data about the Earth from http://cleardarksky.com"""
    
               
    def __init__(self):
        self.earth_info = {}
    
    def get_earth_info(self):
        
        """This gets a web page with predictable output from www.cleardarksky.com and parses it"""        
        
        earth_info = {}
                                    
        # Get the html page from www.cleardarksky.com
        url  = "http://www.cleardarksky.com/txtc/LngLkCCMNcsp.txt"
        
        # Get the data in text version

        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
        data = data.split("blocks = (\n")
        data_table = data[1].splitlines()
 
        # current date
        now = datetime.date.today()

        # tomorrows date
        tomorrow = now + datetime.timedelta(days=1)

        # loop over rows
        for line in data_table:
           if ( line[0:1] != "#" ):
              cols = line.split(",")
        
              datestring1 = cols[0].split("\"")[1]
              datestruct = time.strptime(datestring1,'%Y-%m-%d %H:%M:%S')

              # if today and 7PM or later
              if (datestruct.tm_year == now.year and 
                  datestruct.tm_mon == now.month and
                  datestruct.tm_mday == now.day ):

                  if ( datestruct.tm_hour > 18 ):   
                      print "todays hour, cloud, transp, seeing: ", \
                             datestruct.tm_hour, cols[1], cols[2], cols[3]

                      # determine value for hour
                      # > 7 means less than 30% sky covered
                      # > 2 means average or better transparancy
                      # > 2 means average or better seeing
                      if ( cols[1] > 7 and
                           cols[2] > 2 and
                           cols[3] > 2 ):
                               earth_info[datestruct.tm_hour] = 'a'
                      else:
                               earth_info[datestruct.tm_hour] = 'c'

              # if tomorrow and before 3AM
              if (datestruct.tm_year == tomorrow.year and 
                  datestruct.tm_mon == tomorrow.month and
                  datestruct.tm_mday == tomorrow.day ): 
                  if ( datestruct.tm_hour < 3):   
                      print "tomorrows hour, cloud, transp, seeing: ", \
                             datestruct.tm_hour, cols[1], cols[2], cols[3]

                      if ( cols[1] > 7 and
                           cols[2] > 2 and
                           cols[3] > 2 ):
                               earth_info[datestruct.tm_hour] = 'a'
                      else:
                               earth_info[datestruct.tm_hour] = 'c'
        
              # if we got to 3AM tomorrow we are done
              if (datestruct.tm_year == tomorrow.year and 
                  datestruct.tm_mon == tomorrow.month and
                  datestruct.tm_mday == tomorrow.day ): 
                  if ( datestruct.tm_hour == 3):   
                      break

        # Return all the data     
        return earth_info
    
    def create_string(self):
                                                              
        earth_info = self.get_earth_info()
        print earth_info
            
        str_list = []
        str_list.append("X18")

        for hr in range(19,24):
           str_list.append(earth_info[hr])

        for hr in range(0,3):
           str_list.append(earth_info[hr])

        str_list.append('Z')
                    
        return ''.join(str_list)
        
print "starting main"

clrdrksky = CleardarkskyEarth() 

earth_mess_string = CleardarkskyEarth.create_string(clrdrksky)

print "message string =", earth_mess_string
    

