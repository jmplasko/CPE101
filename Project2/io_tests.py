from lander_funcs import *

def main():
   show_welcome()
   get_altitude()
   get_fuel()
   display_LM_state(12, 1034.278, -54.3333, 486, 7)
   
   # call twice to test with requesting too much fuel
   rate = get_fuel_rate(45)
   print('rate:', rate)
   rate = get_fuel_rate(4)
   print('rate:', rate)
   
   # call three times to display each possible comment
   display_LM_landing_status(-.2)
   display_LM_landing_status(-9)
   display_LM_landing_status(-19)

if __name__ == '__main__':
   main()
