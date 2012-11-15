import sys
import datetime
import urllib2

'''
Created on Apr 5, 2012

@author: tnielsen
'''
class HeavensAboveSun:
    """Scrapes data about the Sun from http://heavens-above.com"""
    
    lat = 0
    lon = 0
    alt = 0
    tz  = "GMT"
               
    def __init__(self, lat, lon, alt, tz):
        """Set the position and altitude information to values"""    
    
        self.lat = lat    
        self.lon = lon    
        self.alt = alt    
        self.tz  = tz  
    
    def get_sun_info(self):
        
        """This gets a web page with predictable output from www.heavens-above.com and parses it"""        
        
        sun_info = []
                                    
        today = datetime.datetime.today()

        year = today.year
        
        # Get the html page from www.heavens-above.com
        url = "http://www.heavens-above.com/sun.aspx?Lat=%f&Lng=%f&tz=%s" % (self.lat, self.lon, self.tz) 
        
        #debug
        #print url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
            
        # Get just the Daily <table> with the data in it from the html
        
        daily_table = data.split(r'<b>Daily')[1]
        daily_table = daily_table.split(r'</table>')[0]
        
        set_time = daily_table.split('Sunset:</td><td>&nbsp;&nbsp;')[1]
        set_time = set_time.split("</td>")[0]
        
        set_time_hr = set_time[0:2]

           
        #print "set time =", set_time
        #print "set time hr", set_time_hr
        
        # Store the data in a dict 
        sun_info = {'set_hr':set_time_hr}            
        
        # Return all the data     
        return sun_info
    
    def create_string(self):
                                                              
        sun_info = self.get_sun_info()
            
        str_list = []
        str_list.append("X28")
        
        #print "set= ", sun_info['set_hr']
        
        for hour_num in range( 19, 27):
            
            set_hr = int (sun_info["set_hr"] )
            
            if ( hour_num == set_hr ):
                str_list.append('b')
            elif ( hour_num > set_hr ):
                str_list.append('a')
            else:
                str_list.append('c')
                    
        str_list.append('Z')
                    
        return ''.join(str_list)
        
# print "starting main"

# ha = HeavensAboveSun(46.4186,-93.5153, 100, "CST")
  
# print ("get info")  

# HeavensAboveSun.get_sun_info(ha)  


# print "sun info: illumination, rise, set", sun_info["illumination"], sun_info["sun_rise_hr"], sun_info["sun_set_hr"]

    
# print "create message string"

# Sun_mess_string = HeavensAboveSun.create_string(ha)

# print "message string =", Sun_mess_string
    

