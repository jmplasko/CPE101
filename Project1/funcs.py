# Project 1
#
# Name: James Plasko
# Instructor: Brian Jones
# Section 21

import math

def pounds_to_kg(pounds):
   return pounds*0.453592

def get_mass_object(obj):
   if obj == 't':
      return 0.1
   elif obj == 'p':
      return  1.0
   elif obj == 'r':
      return  3.0
   elif obj == 'l':
      return 9.07
   elif obj == 'g':
      return 5.3
   else:
      return 0.0

def get_velocity_object(distance):
   return math.sqrt(9.8*distance/2)

def get_velocity_skater(mass_skater, mass_object, velocity_object):
   return get_mass_object(mass_object)*get_velocity_object(velocity_object)/pounds_to_kg(mass_skater)



 
