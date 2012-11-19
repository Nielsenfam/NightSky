import sys
import datetime
import urllib2

'''
Created on Apr 5, 2012

@author: tnielsen
'''
class HeavensAboveMoon:
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
    
    def get_moon_info(self):
        
        """This gets a web page with predictable output from www.heavens-above.com and parses it for all upcoming ISS passes"""        
        
        moon_info = []
                                    
        today = datetime.datetime.today()

        year = today.year
        
        # Get the html page from www.heavens-above.com
        url = "http://www.heavens-above.com/moon.aspx?Lat=%f&Lng=%f&tz=%s" % (self.lat, self.lon, self.tz) 
        
        #debug
        #print url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
    
        # Get just the Appearance <table> with the data in it from the html
        
        appearance_table = data.split(r'<b>Appearance</b>')[1]
        appearance_table = appearance_table.split(r'</table>')[0]
       
        illum = appearance_table.split('PercentIllumination">')[1]
        illum = illum.split("</span")[0]
        
        topo_table = data.split(r'Topocentric Event')[1]
        topo_table = topo_table.split(r'</table>')[0]

        #print "appearance table\n"
        #print appearance_table
        
        
        #print "illum = ", illum
        
        #print "topo table\n"
        #print topo_table
        
        set_time = topo_table.split('SetTime">')[1]
        set_time = set_time.split("</span")[0]
        
        rise_time = topo_table.split('RiseTime">')[1]
        rise_time = rise_time.split("</span")[0]
        
        if set_time[2:3] == ":":
            set_time_hr = int( set_time[0:2] )
        else:
            set_time_hr = -1
            
        if rise_time[2:3] == ":":
            rise_time_hr = int( rise_time[0:2])
        else:
            rise_time_hr = 99
                 
        #print "set time =", set_time
        #print "set time hr", set_time_hr
        #print "rise time =", rise_time
        #print "rise time hr", rise_time_hr

        # Store the data in a dict 
        moon_info = {'set_hr':set_time_hr, 'rise_hr':rise_time_hr,'illum':int(illum)}            
        
        # Return all the data     
        return moon_info
    
    def create_string(self):
                                                              
        moon_info = self.get_moon_info()
            
        str_list = []
        str_list.append("X38")
        
        #print "rise= ", moon_info['rise_hr']
        #print "set= ", moon_info['set_hr']
        
        for hour_num in range( 19, 24):
            
            # moon is out if current hour is between a rise and set or 
            #  if current hour is greater than the rise hour and the rise is greater than the set hour
            rise_hr = moon_info["rise_hr"]
            set_hr = moon_info["set_hr"]
            illum_pct = moon_info["illum"]
                        
            if ( ( (hour_num >= rise_hr) and (hour_num <= set_hr) ) or
                 ( (hour_num >= rise_hr) and (rise_hr >= set_hr ) ) ):
                if (illum_pct > 40 ):
                    if ((hour_num == rise_hr) or (hour_num == set_hr)):
                        str_list.append('b')
                    else:
                        str_list.append('c')
                else:
                    str_list.append('b')
            else:
                str_list.append('a')
            
        # for after midnight, assume next day rise/set is one hour later, a close approximation     
        
        if rise_hr == 99:
            rise_hr = 0
        
        if set_hr == -1:
            set_hr = 99
        
        rise_hr = rise_hr + 1
        if (rise_hr) > 23:
            rise_hr = rise_hr - 24
        set_hr = set_hr + 1
        if (set_hr) > 23:
            set_hr = set_hr - 24
        
            
        for hour_num in range (0, 3):
            if ( ( (hour_num >= rise_hr) and (hour_num <= set_hr) ) or
                 ( (hour_num >= rise_hr) and (rise_hr >= set_hr ) ) ):
                if (illum_pct > 40):
                    if ((hour_num == rise_hr) or (hour_num == set_hr)):
                        str_list.append('b')
                    else:
                        str_list.append('c')
                else:
                    str_list.append('b')
            else:
                str_list.append('a')
                                        
        str_list.append('Z')
                    
        return ''.join(str_list)
        
#print "starting main"

ha = HeavensAboveMoon(46.4186,-93.5153, 100, "CST")  
    
#print "create message string"

Moon_mess_string = HeavensAboveMoon.create_string(ha)

#print "message string =", Moon_mess_string
    
