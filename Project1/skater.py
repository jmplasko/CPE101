# Project 1
#
# Name: James Plasko
# Instructor: Brian Jones
# Section: 21

import funcs

def main():
   weight = float(input("How much do you weigh (pounds)? "))
   dis = float(input("How far away is your professor (meters)? "))
   choice = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ightsaber, or lawn (g)nome? ")
   mass = funcs.get_mass_object(choice)

   if mass<=0.1:
      print("\nNice throw! You're going to get an F!")
   elif mass>0.1 and mass<=1.0:
      print("\nNice throw! Make sure your professor is OK.")
   else:
      if dis < 20:
         print("\nNice throw! How far away is the hospital?")
      else:
         print("\nNice throw! RIP professor.")

   velocity = funcs.get_velocity_skater(weight,choice,dis)
   print("Velocity of skater: {:.3f} m/s".format(velocity))

   if velocity < 0.2:
      print("My grandmother skates faster than you!")
   elif velocity < 1.0 and velocity >= 0.2:
      pass
   else:
      print("Look out for that railing!!!")

if __name__ == "__main__":
   main()

