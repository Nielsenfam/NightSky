Night Sky Orb

By Terry Nielsen

The Night Sky Orb is a RaspberryPi based "clock" that gives a quick summary
of the objects visible in the night sky for the current night by turning 
on/off an LED representative of each hour in the night.

Status:

Two versions: 

Tk based GUI: LEDgrid.py
i2c version: LEDgridDrive.py

LEDgridDrive.py needs to be run as root and should be run on startup. 
It will drive a LED matrix connected to the i2c port of the raspberry pi. 

Notes: 

1. LED driver version needs more testing
2. Setting LEDs to a dim state not working (not sure how to make work)


Objects supported inlcude:

Earth: Displays an indication of the cloud cover, transparancy, and seeing
   on indicates "mostly clear and at least avg transparency and avg seeing"
   off indicates "not clear or poor transparancy or poor seeing"

Sun: Indicates time of sunset/sunrise "on" is sun is out.

Moon: Indicates when the moon is visible, "on" is moon is out, brightness 
    indicates how bright the moon is.

ISS: Any International Space Station Passes, count the # of flashes 
    to tell what the 10 minute period of the hour it is visible.

Venus: On indicates Venus is visible that hour 

Mars: On indicates Mars is visible that hour

Saturn: On indicates Saturn is visible that hour

Jupiter: On indicates Jupiter is visible that hour


Originally designed for an 8x8 LED matrix to go from hours 7PM to 2AM and 
driven directly by an Ardino with a wifi connection to the code on a 
seperate server.

Redesigned for RaspberryPi, with local code connected to a wifi dongle 
and an LED matrix driven by i2c bus driver.

Sky information is obtained by "screen scraping" heavens-above.com. Wish
there was a xml service so it could be more robust. 


Enhancement Ideas:

1. A possible enhancement would be to do the Sun, Moon and Planet calculations
localy using the apropriate astronimcal calculations. Shouldn't be that hard,
people have been doing those calculations for centuries! That would leave only 
the ISS and weather data to be "screen scraped".

2. The i2c LED matrix could be larger to cover 12 hours for the whole "night". 
Might be easier to use a second Backpack at a different address

3. The Earth Sky conditions could display additional observing conditions 
such as those found on cleardarksky.com.

4. i2c could also drive additional 7 segement display for 
traditional "clock" functionality.

Combined with Above, a pushbutton could be used to display exact 
times of Rise/Set on a 7 segment display
