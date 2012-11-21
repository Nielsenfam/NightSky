import ephem
import datetime
import pytz



def calc_status( rise_tm, set_tm, clocktm ):
    
#
# function to calculate the clock light status based upon rise and set time for a given hour
#
# 6 possible cases, truth table:
#    
#  First Second Last   Display
# 1  RT    ST     CL      OFF     
# 2  ST    RT     CL      ON
# 3  RT    CL     ST      ON
# 4  ST    CL     RT      OFF
# 5  CL    ST     RT      ON
# 6  CL    RT     ST      OFF
#
# key:
#   RT = rise date/time
#   ST = set date/time
#   CL = clock date/time being evaluated

    # 1. case where rise time is before set time
    #     and the set time is before the clock time
    #
    if ( rise_tm < set_tm and
         set_tm < clocktm ):
        clock_status = "off"
        #print "case 1:", clock_status

    # 2. case where set time is before the rise time
    #     and rise time is before the clock time
    if ( set_tm < rise_tm and
         rise_tm < clocktm ):
        clock_status = "on"
        #print "case 2:", clock_status

    # 3. case where rise time is before the clock time
    #     and clock time is before the set time
    if ( rise_tm < clocktm and
         clocktm < set_tm ):
        clock_status = "on"
        #print "case 3:", clock_status
    
    # 4. case where set time is before clock time
    #     and the clock time is before the rise time
    #
    if ( set_tm < clocktm and
         clocktm < rise_tm ):
        clock_status = "off"
        #print "case 4:", clock_status

    # 5. case where clock time is before the set time
    #     and set time is before the rise time
    if ( clocktm < set_tm and
         set_tm < rise_tm ):
        clock_status = "on"
        #print "case 5:", clock_status

    # 6. case where clock time is before the rise time
    #     and rise time is before the set time
    if ( clocktm < rise_tm and
         rise_tm < set_tm ):
        clock_status = "off"
        #print "case 6:", clock_status

    return clock_status;



# local inforamtion to be parameterized
lat = 46.4186
lon = -93.5153
alt = 100
tz = 'US/Central'

# time of clock start and end in military time
clock_start_hr = 19
clock_end_hr = 03

# dictonary for rise, set times and row string
set_tm_d = {}
rise_tm_d = {}
row_string_d = {}

# use time of 4PM today for all calculations so that it always gets next rise and set times for this evening

mytz = pytz.timezone(tz)
eptz = pytz.timezone('utc')

now = datetime.date.today()
afternoon = mytz.localize( datetime.datetime(now.year,now.month,now.day)+ datetime.timedelta(hours=16))
eptafternoon = afternoon.astimezone(eptz)
# print "eptafternoon", eptafternoon

# define objects
sun = ephem.Sun()
moon = ephem.Moon()
venus = ephem.Venus()
mars = ephem.Mars()
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()

# setup current location
here = ephem.Observer()
here.lon = str(lon)
here.lat = str(lat)
here.elev = alt
here.date = eptafternoon
# print here

# compute objects based upon current location
sun.compute(here)
moon.compute(here)
venus.compute(here)
mars.compute(here)
jupiter.compute(here)
saturn.compute(here)

sun_r = ephem.localtime(here.next_rising(sun))
sun_s = ephem.localtime(here.next_setting(sun))
rise_tm_d[ "sun" ] = sun_r
set_tm_d[ "sun" ] = sun_s

moon_r = ephem.localtime(here.next_rising(moon))
moon_s = ephem.localtime(here.next_setting(moon))
rise_tm_d[ "moon" ] = moon_r
set_tm_d[ "moon" ] = moon_s

venus_r = ephem.localtime(here.next_rising(venus))
venus_s = ephem.localtime(here.next_setting(venus))
rise_tm_d[ "venus" ] = venus_r
set_tm_d[ "venus" ] = venus_s

mars_r = ephem.localtime(here.next_rising(mars))
mars_s = ephem.localtime(here.next_setting(mars))
rise_tm_d[ "mars" ] = mars_r
set_tm_d[ "mars" ] = mars_s

jupiter_r = ephem.localtime(here.next_rising(jupiter))
jupiter_s = ephem.localtime(here.next_setting(jupiter))
rise_tm_d[ "jupiter" ] = jupiter_r
set_tm_d[ "jupiter" ] = jupiter_s

saturn_r = ephem.localtime(here.next_rising(saturn))
saturn_s = ephem.localtime(here.next_setting(saturn))
rise_tm_d[ "saturn" ] = saturn_r
set_tm_d[ "saturn" ] = saturn_s

# print "sun r,s:", sun_r, sun_s
# print "moon r,s:", moon_r, moon_s
# print "venus r,s:", venus_r, venus_s 
# print "mars r,s:", mars_r, mars_s
# print "jupiter_r,s:", jupiter_r, jupiter_s
# print "saturn_r,s:", saturn_r, saturn_s


for object in ("sun","moon","venus","mars","jupiter","saturn"):

    row_string = "X11"
    rise_tm = rise_tm_d[ object ]
    set_tm = set_tm_d[ object ]
    print object, rise_tm, set_tm
    for hr in range( clock_start_hr,24):
        LED_status = "none"
        clocktm = datetime.datetime(now.year,now.month,now.day)+ datetime.timedelta(hours=hr)
        LED_status = calc_status( rise_tm, set_tm, clocktm )
        # print LED_status
        if (LED_status == "on"):
            row_string = row_string + "c"
        else:
            row_string = row_string + "a"

    for hr in range( 0, clock_end_hr):
        LED_status = "none"
        clocktm = datetime.datetime(now.year,now.month,now.day+1)+ datetime.timedelta(hours=hr)
        LED_status = calc_status( rise_tm, set_tm, clocktm )
        # print LED_status
        if (LED_status == "on"):
            row_string = row_string + "c"
        else:
            row_string = row_string + "a"

    row_string = row_string + "Z"
    print row_string
    row_string_d[ object ] = row_string

for obj in row_string_d:
    print obj, row_string_d[ obj ]
    
