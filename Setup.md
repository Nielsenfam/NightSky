
Instructions to setup a Raspberry Pi to run the NightSkyOrb
===========================================================

Set up new SD card with raspbian distribution
---------------------------------------------

Insert SD card and do config:
     Expand to full card, reset password, set timezone

setup wifi
----------

Using gui tool on desktop

setup keyboard
--------------

# sudo vi /etc/default/keyboard and change "gb" to "us"

reboot after that

# sudo reboot

get current updates
-------------------

In terminal window do this to get to most current packages:

# sudo apt-get update
# sudo apt-get upgrade

setup python development environment
------------------------------------

In terminal window get python development environment and python install package tool

# sudo apt-get install python-pip python-dev


setup necessary python packages for astronomical calculations
-------------------------------------------------------------

get stuff for calculating ephem by getting pyephem and putz packages:

# sudo pip install pyephem pytz


setup git so we can retrieve code
---------------------------------

get git so we can get NightSky code:

# sudo apt-get install git

retrieve code from github:

# git clone http://github.com/Nielsenfam/NightSky

Setup for GPIO and i2c access from python
-----------------------------------------

# sudo apt-get install python-rpi.gpio

# sudo apt-get install python-smbus i2c-tools

Now enable gpio and smbus access from kernel:

# sudo vi /etc/modules

in editor add these two lines to end of file:

    i2c-bcm2708 
    i2c-dev

And also need to remove from blacklist

# sudo vi /etc/modprobe.d/raspi-blacklist.conf

in vi comment out two lines:

blacklist spi-bcm2708
blacklist i2c-bcm2708

And finally need to reboot to get kernel updated

# reboot

Configuring and Validation
--------------------------

To validate it all works:

Edit params.py to match location:

# vi params.py

Change latitude, longitude, and cleardarksky location

# sudo python LEDgrid.py

if all is working should see desktop graphical "LED" version of the NightSkyOrb

Now test the LED matrix grid version: 

RiPi needs to have LED 8x8 grid backpack connected to GPIO, see instructions from Adafruit

# sudo i2cdetect -y 0

Change to 1 if on 512Mb

should see 70 if backpack is connected

Now test LED grid by typing this:

# sudo test_LEDmatrix.py

LED matrix should scan all elements

Now run the LEDgridDrive.py version:

# sudo python LEDgridDrive.py

If it all works, the LEDs should look same as the desktop graphical LED orb


