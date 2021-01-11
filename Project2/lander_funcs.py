# Project 2 - Moonlander
#
# Name: James
# Instructor: Brian Jones
# Section: 21

def show_welcome():
   print()
   print("Welcome aboard the Lunar Module Flight Simulator")
   print()
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print()
   print("   Good luck and may the force be with you!")
   print()

def get_altitude():
   altitude = float(input("Enter the initial altitude of the LM (in meters): "))
   while altitude < 1 or altitude > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      print()
      altitude = float(input("Enter the initial altitude of the LM (in meters): "))

   return altitude

def get_fuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   while fuel < 1:
      print("ERROR: Amount of fuel must be positive, please try again")
      print()
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))

   return fuel
   
def display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
   print("Elapsed Time:{:>5d} s".format(elapsed_time))
   print("        Fuel:{:>5d} l".format(fuel_amount))
   print("        Rate:{:>5d} l/s".format(fuel_rate))
   print("    Altitude:{:>8.2f} m".format(altitude))
   print("    Velocity:{:>8.2f} m/s".format(velocity))

def get_fuel_rate(current_fuel):
   fuel_burn  = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while fuel_burn < 0 or fuel_burn > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive")
      print()
      fuel_burn = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
 
   if fuel_burn > current_fuel:
      return current_fuel
   else:
      return fuel_burn

def display_LM_landing_status(velocity):
   if velocity <= 0 and velocity >= -1:
      print("Status at landing - The eagle has landed!")
   elif velocity < -1 and velocity > -10:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   else:
      print("Status at landing - Ouch - that hurt!")
 
def update_acceleration(gravity, fuel_rate):
   acceleration = gravity * (fuel_rate/5 - 1)
   return acceleration

def update_altitude(altitude, velocity, acceleration):
   altitude_new = altitude + velocity + acceleration/2
   if altitude_new < 0:
      altitude_new = 0

   return altitude_new

def update_velocity(velocity, acceleration):
   velocity_new = velocity + acceleration
   return velocity_new

def update_fuel(fuel, fuel_rate):
   fuel_new = fuel-fuel_rate
   return fuel_new
