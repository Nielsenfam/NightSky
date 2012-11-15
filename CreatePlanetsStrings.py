import sys
import datetime
import urllib2

'''
Created on Apr 5, 2012

@author: tnielsen
'''
class HeavensAbovePlanet:
    """Scrapes data about the Moon from http://heavens-above.com"""
    
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
    
    def get_planet_info(self):
        
        """This gets a web page with predictable output from www.heavens-above.com and parses it for all upcoming ISS passes"""        
              
        data_table = []
        planet_info = {}
                                    
        today = datetime.datetime.today()

        year = today.year
        
        # Get the html page from www.heavens-above.com
        url = "http://www.heavens-above.com/PlanetSummary.aspx?Lat=%f&Lng=%f&tz=%s" % (self.lat, self.lon, self.tz) 
        
        #debug
        #print url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data_table = response.read()
        
        # Get just the Planet <table> with the data in it from the html
                
        planet_table = data_table.split(r'Rises')[1]
        planet_table = planet_table.split(r'Altitude')[0]

        #print "planet table\n"
        #print planet_table

        rise_times = planet_table.split(r'"center">')       
        
        # mercury rise time 
        rise_time_str = rise_times[1]
        rise_time_str = rise_time_str.split(r'</td>')[0] 
        #print "mer rise time", rise_time_str
        planet_info["mercury rise hour"] = self.get_rise_hour( rise_time_str )
        
        # venus rise time 
        rise_time_str = rise_times[2]
        rise_time_str = rise_time_str.split(r'</td>')[0] 
        #print "ven rise time", rise_time_str
        planet_info["venus rise hour"] = self.get_rise_hour( rise_time_str)       
        
        # mars rise time 
        rise_time_str = rise_times[3]
        rise_time_str = rise_time_str.split(r'</td>')[0] 
        #print "mars rise time", rise_time_str
        planet_info["mars rise hour"] = self.get_rise_hour( rise_time_str)
        
        # jupiter rise time 
        rise_time_str = rise_times[4]
        rise_time_str = rise_time_str.split(r'</td>')[0] 
        #print "jup rise time", rise_time_str
        planet_info["jupiter rise hour"] = self.get_rise_hour( rise_time_str)
        
        # saturn rise time 
        rise_time_str = rise_times[5]
        rise_time_str = rise_time_str.split(r'</td>')[0] 
        #print "sat rise time", rise_time_str
        planet_info["saturn rise hour"] = self.get_rise_hour( rise_time_str)
 
        # now get Set Times
 
        planet_table = data_table.split(r'Sets')[1]
        planet_table = planet_table.split(r'Altitude')[0]

        #print "planet table for Sets\n"
        #print planet_table

        set_times = planet_table.split(r'"center">')       
        
        # mercury set time 
        set_time_str = set_times[1]
        set_time_str = set_time_str.split(r'</td>')[0] 
        # print "mer set time", set_time_str
        planet_info["mercury set hour"] = self.get_set_hour( set_time_str)
        
        # venus set time 
        set_time_str = set_times[2]
        set_time_str = set_time_str.split(r'</td>')[0] 
        # print "ven set time", set_time_str
        planet_info["venus set hour"] = self.get_set_hour( set_time_str)
               
        # mars set time 
        set_time_str = set_times[3]
        set_time_str = set_time_str.split(r'</td>')[0] 
        # print "mars set time", set_time_str
        planet_info["mars set hour"] = self.get_set_hour( set_time_str)
        
        # jupiter set time 
        set_time_str = set_times[4]
        set_time_str = set_time_str.split(r'</td>')[0] 
        # print "jup set time", set_time_str
        planet_info["jupiter set hour"] = self.get_set_hour( set_time_str)
        
        # saturn set time 
        set_time_str = set_times[5]
        set_time_str = set_time_str.split(r'</td>')[0] 
        # print "sat set time", set_time_str
        planet_info["saturn set hour"] = self.get_set_hour( set_time_str)
            
        return planet_info
    
    def get_set_hour(self, set_str):
                
        if set_str[2:3] == ":":
            set_hr = int( set_str[0:2] )
        else:
            set_hr = -1
        
        #print "set time =", set_time
        #print "set hr", set_hr
        
        return set_hr

    def get_rise_hour(self, rise_str):
            
        if rise_str[2:3] == ":":
            rise_hr = int( rise_str[0:2])
        else:
            rise_hr = 99
                 
        #print "rise time =", rise_time
        #print "rise hr", rise_hr
        
        # Return all the data     
        return rise_hr
    
    def create_string(self, rise_hr, set_hr):
 
 
        str_list = []                                                                     

        for hour_num in range( 19, 24):
                        
            # planet is out if current hour is between a rise and set or if current hour is greater than the set and the set is greater rise
            
            if ( ( (hour_num >= rise_hr) and (hour_num <= set_hr) ) or
                 ( (hour_num >= rise_hr) and (rise_hr > set_hr ) ) ):
                if ( ( hour_num == rise_hr) or ( hour_num == set_hr ) ):
                    str_list.append('b')
                else:
                    str_list.append('c')
            else:
                str_list.append('a')
                                    
        if rise_hr < 8:
            rise_hr = rise_hr + 24
        if set_hr < 8:
            set_hr = set_hr + 24


        # for planets it is OK to assume rise/set is approximate same time on following day, consider hours past midnight
        for hour_num in range( 24, 27):
                        
            # planet is out if current hour is between a rise and set or if current hour is greater than the set and the set is greater rise
            # print "past midnight hour_num:", hour_num
            if ( ( (hour_num >= rise_hr) and (hour_num <= set_hr) ) or
                 ( (hour_num >= rise_hr) and (rise_hr > set_hr ) ) ):
                if ( ( hour_num == rise_hr) or ( hour_num == set_hr ) ):
                    str_list.append('b')
                else:
                    str_list.append('c')
            else:
                str_list.append('a')
                                    
                                    
        str_list.append('Z')
                    
        return ''.join(str_list)

    def create_all_strings( self ):

        all_planet_strings = []
                        
        planet_info = self.get_planet_info()
        
        # venus info
        
        venus_str_list = []
        venus_str_list.append("X58")
        rise_hr = planet_info["venus rise hour"]
        set_hr = planet_info["venus set hour"]
        
        end_string = self.create_string(rise_hr, set_hr)
        venus_str_list.append(end_string)
        
        venus_str = ''.join(venus_str_list)
        #print "venus rise, set hour", rise_hr, set_hr
        #print "venus string :"
        #print venus_str
        all_planet_strings.append(venus_str)

       # mars
        
        mars_str_list = []
        mars_str_list.append("X68")
        rise_hr = planet_info["mars rise hour"]
        set_hr = planet_info["mars set hour"]
        
        end_string = self.create_string(rise_hr, set_hr)
        mars_str_list.append(end_string)
        
        mars_str = ''.join(mars_str_list)
        #print "mars rise, set hour", rise_hr, set_hr
        #print "mars string :"
        #print mars_str
        all_planet_strings.append(mars_str)
 
       # jupiter
        
        jup_str_list = []
        jup_str_list.append("X78")
        rise_hr = planet_info["jupiter rise hour"]
        set_hr = planet_info["jupiter set hour"]
        
        end_string = self.create_string(rise_hr, set_hr)
        jup_str_list.append(end_string)
        
        jup_str = ''.join(jup_str_list)
        #print "jup rise, set hour", rise_hr, set_hr
        #print "jup string :"
        #print jup_str
        all_planet_strings.append(jup_str)


       # saturn
        
        sat_str_list = []
        sat_str_list.append("X88")
        rise_hr = planet_info["saturn rise hour"]
        set_hr = planet_info["saturn set hour"]
        
        end_string = self.create_string(rise_hr, set_hr)
        sat_str_list.append(end_string)
        
        sat_str = ''.join(sat_str_list)
        #print "sat rise, set hour", rise_hr, set_hr
        #print "sat string :"
        #print sat_str
        all_planet_strings.append(sat_str)
        
        return all_planet_strings
        
#print "starting main"

#ha = HeavensAbovePlanet(46.4186,-93.5153, 100, "CST")
  
#print ("get info")  

#HeavensAboveMoon.get_moon_info(ha)  

#all_planet_strings = []

#all_planet_strings = HeavensAbovePlanet.create_all_strings(ha)

#for i, aplanet in enumerate(all_planet_strings):      
            
#    planet_string = aplanet
#    print "i, string", i, planet_string


    

