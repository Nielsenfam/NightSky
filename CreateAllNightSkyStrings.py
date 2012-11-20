'''
Created on Apr 10, 2012

@author: tnielsen
'''

import CreateISSInfoString
import CreateMoonString
import CreatePlanetsStrings
import CreateSunString
import CreateEarthString

class CreateAllNightSkyStrings:
    
    haISS = []
    haMoon = []
    haPlanets = []
    haSun = []
    Earth = []

    def __init__(self):
        
        lat = 46.4186
        lon = -93.5153
        alt = 100
        tz = "CST"
        
        # initialze all objects
        self.haISS = CreateISSInfoString.HeavensAboveISS( lat, lon, alt, tz )
        self.haMoon = CreateMoonString.HeavensAboveMoon( lat, lon, alt, tz )
        self.haPlanets = CreatePlanetsStrings.HeavensAbovePlanet( lat, lon, alt, tz)
        self.haSun = CreateSunString.HeavensAboveSun( lat, lon, alt, tz )
        self.Earth = CreateEarthString.CleardarkskyEarth( )
        
    def get_all_NS_strings(self):
        
        all_NS_strings = []
        
        # earth
        all_NS_strings.append( self.Earth.create_string() )
        
        # sun
        all_NS_strings.append( self.haSun.create_string() )
        
        # moon
        all_NS_strings.append( self.haMoon.create_string() )
        
        # ISS
        all_NS_strings.append( self.haISS.create_string() )
        
        # Venus
        all_NS_strings.append( self.haPlanets.create_all_strings()[0] )
        
        # Mars
        all_NS_strings.append( self.haPlanets.create_all_strings()[1] )

        # Jupiter
        all_NS_strings.append( self.haPlanets.create_all_strings()[2] )

        # Saturn
        all_NS_strings.append( self.haPlanets.create_all_strings()[3] )

        
        return all_NS_strings



# all_NS_objects = CreateAllNightSkyStrings()
    
# all_NS_strings = all_NS_objects.get_all_NS_strings()

# for i, aNightSkyString in enumerate(all_NS_strings):      
            
#   NS_object_string = aNightSkyString
#   print "i, string", i, NS_object_string


        
        
