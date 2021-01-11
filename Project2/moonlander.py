# Project 2 - Moonlander
#
# Name: James Plasko
# Instructor: Brian Jones
# Section: 21

from lander_funcs import *

def main():
   show_welcome()
   altitude = get_altitude()
   fuel = get_fuel()
   time = 0
   velocity = 0
   fuel_rate = 0
   print()
   print("LM state at retrorocket cutoff")
   display_LM_state(time, altitude, velocity, fuel, fuel_rate)
   print()

   while altitude > 0:
      if fuel > 0:
         fuel_rate_user = get_fuel_rate(fuel)
         fuel = update_fuel(fuel, fuel_rate_user)
      else:
         fuel_rate_user = 0

      time += 1
      acceleration = update_acceleration(1.62, fuel_rate_user)
      altitude = update_altitude(altitude, velocity, acceleration)
      velocity = update_velocity(velocity, acceleration)
      if altitude == 0:
         print()
         print("LM state at landing/impact")
      if fuel > 0 or altitude == 0:
         display_LM_state(time, altitude, velocity, fuel, fuel_rate_user)
         print()
      else:
         print("OUT OF FUEL - Elapsed Time:{:>4d} Altitude:{:>8.2f} Velocity:{:>8.2f}".format(time, altitude, velocity))

   display_LM_landing_status(velocity)


if __name__ == '__main__':
   main()
