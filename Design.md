Project Idea: Quick View Night Sky Summary Display
==================================================

Name: NightSkyOrb
-----------------

Queries server each day to get status of sun rise/set, moon rise/set, planets visible, weather summary, and ISS passes.

Do as a "grid" of 8 x 8 LEDs:

- For each body show visible TOD: 7,8,9,10,11,12,1,2

- Off = not visible, dim = rising/setting, bright = in sky
	
1. Earth (Sky): Earth: Off = Cloudy, Dim = Party Cloudy, Bright = Clear Skys
2. Sun: Sun: On = visible, Off = not visible (or should this reverse?)
3. Moon: Moon: Off = not visible, dim = 0-20 degrees, dim = above 20 degrees but less than half full, bright = above 20 degrees, more than half full
4. ISS: Off = not visible, Visible Pass, flashes 1 time for every 10 minutes past hour
5. Venus: Bright = In Sky, above 10 degrees, Dim = 0-20 degrees, Off = not visible
6. Mars: Bright = In Sky, above 10 degrees, Dim = 0-20 degrees, Off = not visible
7. Jupiter: Bright = In Sky, above 20 degrees, Dim = 0-20 degrees, Off = not visible
8. Saturn: Bright = In Sky, above 20 degrees, Dim = 0-20 degrees, Off = not visible


Serial Protocol:
----------------
Originally designed to communicate to Arduino, not really needed now


header: 'X', 
row num=0-9, 
col count=8, 
ascii data string one char per column, footer: 'Z\n',  

info for each LED: 
	
+ a = off
+ b = dim
+ c = on/bright
+ d = slow flash 10 secs on, 10 off	
+ f = slow flash 10 seconds on 10 off
+ g = 1 flash: 1 sec on, 1 off, 10 off (for minutes :00-09:59)
+ h = 2 flash: 1 on, 1 off, 1 on, 1 off, 10 sec off (for minutes :10-19:59)
+ i = 3 flash: 1 on, 1 off, 1 on, 1 off, 1 on, 1 off, 10 off (for minutes :20-29:59)
+ j = 4 flash: 4x 1 on/off, 10 off (for minutes :30-39:59)
+ k = 5 flash: 5x 1 on/off, 10 off (for minutes :40-49:59)
+ l = 6 flash: 6x 1 on/off, 10 off (for minutes :50-59:59)

Example: row 2 is for sun setting in 9PM hour:
		X28ccbaaaaaZ\n
		
Example: row 3 is for near full moon rising at 10PM:
		X38aaabccccZ\n
		
Example: row 4 is for ISS making a visible pass at 10:35PM
		X48aaajaaaaZ\n
		
Example: row 6 is for Mars visible from sunset (9PM) till 11PM, going to 20 degrees from horizon in 10PM hour
		X46aabcbaaaZ\n 	

LED display:
------------

Now using Adafruit LED backpack
 		
Put individual LEDs into a picture frame?

http://www.flickr.com/photos/spikenzie/3674197080/in/set-72157603968192071/	
 		
from: http://www.spikenzielabs.com/SpikenzieLabs/Main.html
http://www.spikenzielabs.com/SpikenzieLabs/8x8.html	

with LEDS could color code by object:
+ Sun: Yellow
+ Earth: Blue
+ Moon: White
+ ISS: Blue
+ Venus: Yellow
+ Mars: Red
+ Jupiter: Orange
+ Saturn: Yellow
	

Original Sketch in ppt, convert to another format
-------------------------------------------------

A row of LEDS for each object, and then a label on the top or side of the object for hours?
	
Time is on the X axis. 
	
	
Use IKEA picture frame

LEDs in http://www.spikenzielabs.com/SpikenzieLabs/8x8.html 


Older Version:
--------------

Notify

- Off = nothing today, or nothing more today (till 8AM)
- On - Dim White - something tonight
- On - Slow Flashing Dim White (on 15 sec, off 5 sec) - in 1-3 hours
- On - Fast Bright White flashing - N quick 2 sec on/off flashes then off 15 seconds, repeats, N*10 minutes
- On - Bright White No Flashing - overhead

Clear Sky Forecast

Planets Visible

White = Moon, brightness = phase
Red = Mars brlight visible before midnight, dim visiible after midnight
Blue = Venus
Yellow = Saturn
Orange = Jupiter

Sky 

Blue On No Clouds, Good Transparancy
Blue Off = Cloudy, Poor Transparancy
