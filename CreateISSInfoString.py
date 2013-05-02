
# import sys
import urllib2
import ephem
import datetime
import pytz
import params


'''
Created on Apr 5, 2012

@author: tnielsen
'''
class EphemISS:
    """Scrapes data about the ISS from http://heavens-above.com"""
    
    lat = 0
    lon = 0
    alt = 0
    tz  = "GMT"
               
    def __init__(self, lat, lon, alt, tz):
        """Set the position and altitude information to values"""    
    
        self.lat = params.lat    
        self.lon = params.lon    
        self.alt = params.alt    
        self.tz  = params.tz  
    
    def get_passes(self):


        passes_dict = []

        # use time of 4PM today for all calculations so that it always gets next rise and set times for this evening

        mytz = pytz.timezone(self.tz)
        eptz = pytz.timezone('utc')

        now = datetime.date.today()
        afternoon = mytz.localize( datetime.datetime(now.year,now.month,now.day)+ datetime.timedelta(hours=16))
        eptafternoon = afternoon.astimezone(eptz)
        # print "eptafternoon", eptafternoon

        # setup current location
        here = ephem.Observer()
        here.lon = str(self.lon)
        here.lat = str(self.lat)
        here.elev = self.alt
        here.date = eptafternoon
        # print here

        # do lookup from NASA website:
       
        url = params.nasa_url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()

        # look for TWO LINE MEAN ELEMENT SET in file
        table = data.split("TWO LINE MEAN ELEMENT SET")[1]
        line1 = table.splitlines()[3]
        line2 = table.splitlines()[4]
        # print "line 1:", line1
        # print "line 2:", line2
        
        iss = ephem.readtle('ISS', \
                            line1, \
                            line2)


        # get next 5 passes, there would never be more than 5 passes after 4PM
        for apass in range(0,5):
            iss.compute(here)

            iss_np = here.next_pass(iss)
            iss_r = ephem.localtime(iss_np[0])
            iss_s = ephem.localtime(iss_np[4])
            # print "pass n: iss rise, set:", apass, iss_r, iss_s

        
            # Store the data in a list      
            passes_dict.append({"begin_time": iss_r, "end_time": iss_s})

            here.date = iss_np[4]
        
        # Return all the data     
        return passes_dict  

    def get_todays_pass(self):    
        """This will try and get all the upcoming passes from www.heavens-above.com and store the data for today's passes"""
    
        todays_passes_dict = []
        now = datetime.datetime.today()
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        
        # print "now date/time = ", now.year, now.month, now.day 
                    
       
        # Get all passes
        passes = self.get_passes()
            
        # Loop through the passes and find all that are for this day
        for apass in passes:
            this_pass = apass["begin_time"]     
            if ( (this_pass.day == now.day) and (this_pass.month == now.month) and ( this_pass.hour > 10) ): 
                todays_passes_dict.append({"begin_time": this_pass})
            elif ( (this_pass.day == tomorrow.day) and (this_pass.month == tomorrow.month ) and ( this_pass.hour < 8 ) ):
                todays_passes_dict.append({"begin_time": this_pass})                                    
  
        return todays_passes_dict
    
    def create_string(self):
                                                              
        todays_passes = self.get_todays_pass()
            
        str_list = []
        str_list.append("X48")
        
        for hour_num in range( params.start_hr, params.end_hr+24):
            
            string_set = 0   
            for apass in todays_passes:
                this_pass = apass["begin_time"]
                this_pass_min = this_pass.minute

                # if the hour is less than 8 AM, it is for tomorrow morning
                if (this_pass.hour > 8):
                    this_pass_hr = this_pass.hour
                else:
                    this_pass_hr = this_pass.hour + 24
                    
                if (this_pass_hr == hour_num):
                    if(this_pass_min < 10):
                        str_list.append('g')
                    elif (this_pass_min < 20):
                        str_list.append('h')
                    elif (this_pass_min < 30):
                        str_list.append('i')
                    elif (this_pass_min < 40):
                        str_list.append('j')
                    elif (this_pass_min < 50):
                        str_list.append('k')
                    else:
                        str_list.append('l')
                            
                    string_set = 1
                    break
            if string_set == 0:
                str_list.append('a')
                    
        str_list.append('Z')
                    
        return ''.join(str_list)
        
##print "starting main"
##
##ha = EphemISS(params.lat,params.lon, params.alt, params.tz)
##          
##print( "get today's passes")    
##todays_passes = EphemISS.get_todays_pass(ha)
##
##print "today's passes:"
##for apass in todays_passes:
##   this_pass = apass["begin_time"]
##   print "month/day/hour/min", this_pass.month,this_pass.day,this_pass.hour,this_pass.minute
##    
##print "create message string"
##
##ISS_mess_string = EphemISS.create_string(ha)
##
##print "message string =", ISS_mess_string
    

        
        
