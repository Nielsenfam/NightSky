
import sys
import datetime
import urllib2

'''
Created on Apr 5, 2012

@author: tnielsen
'''
class HeavensAboveISS:
    """Scrapes data about the ISS from http://heavens-above.com"""
    
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
    
    def get_passes(self):
        
        """This gets a web page with predictable output from www.heavens-above.com and parses it for all upcoming ISS passes"""        
                                    
        today = datetime.datetime.today()

        year = today.year
        passes_dict = []
        
        # Get the html page from www.heavens-above.com
        url = "http://www.heavens-above.com/PassSummary.aspx?showAll=t&satid=25544&lat=%f&lng=%f&alt=%0.0f&tz=%s" % (self.lat, self.lon, self.alt, self.tz)
        
        #debug
        # print url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
    
        # Get just the <table> with the data in it from the html
        
        table = data.split(r'<table id=')[1]
        table = table.split(r'</table>')[0]
        
        
        # Break out each row in the table, skip the first two (just contains metadata)
        passes = table.split('<tr class=')[3:]
        
        # print passes
        
        # Go through each row    
        for i, apass in enumerate(passes):      
            
            # split the row into cells
            details = apass.split('<td')
                          
            # parse the data out into variables
        
            date          = details[1][-15:-9].strip()
            begin_time    = details[2][1:9].strip()        
            begin_alt     = details[3][16:18].strip()      
            begin_az      = details[4][1:4].strip()
            max_time      = details[5][1:9].strip()
            max_alt       = details[6][16:18].strip()
            max_az        = details[7][1:4].strip()
            end_time      = details[8][1:9].strip()
            end_alt       = details[9][16:18].strip()
            end_az        = details[10][1:4].strip()
                                                  
            # further parse the date
            day   = date[0:2]
            month = date[3:]
            
            #debug      
            # print i, date, month, day, begin_time, begin_alt, begin_az, max_time, max_alt, max_az, end_time, end_alt, end_az
        
            # Find the beginning and ending dates and turn them into datetime objects
            begin_datetime  = datetime.datetime.strptime("%d-%s-%s %s" % (year, month, day, begin_time), "%Y-%b-%d %H:%M:%S")
            end_datetime    = datetime.datetime.strptime("%d-%s-%s %s" % (year, month, day, end_time),   "%Y-%b-%d %H:%M:%S")
                                        
            #debug      
            # print i, begin_datetime, end_datetime
        
            # Store the data in a list      
            passes_dict.append({"begin_time": begin_datetime, "end_time": end_datetime})
        
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
        
        for hour_num in range( 19, 27):
            
            string_set = 0   
            for apass in todays_passes:
                this_pass = apass["begin_time"]
                this_pass_min = this_pass.minute
                
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
        
#print "starting main"

#ha = HeavensAboveISS(46.4186,-93.5153, 100, "CST")
          
#print( "get today's passes")    
#todays_passes = HeavensAboveISS.get_todays_pass(ha)

#print "today's passes:"
#for apass in todays_passes:
#    this_pass = apass["begin_time"]
#    print "month/day/hour/min", this_pass.month,this_pass.day,this_pass.hour,this_pass.minute
    
#print "create message string"

#ISS_mess_string = HeavensAboveISS.create_string(ha)

#print "message string =", ISS_mess_string
    

        
        