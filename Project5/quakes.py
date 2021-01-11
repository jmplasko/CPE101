from quake_funcs import *

def main():
   quakes = read_quakes_from_file("quakes.txt")
   next_ans = 'a'
   table_stuff(quakes)
   while next_ans != 'q':
      print("Options:")
      print("  (s)ort")
      print("  (f)ilter")
      print("  (n)ew quakes")
      print("  (q)uit")
      print()
      ans= input("Choice: ")
      if ans == 's' or ans == 'S':
         new = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
         print()
         new = new.lower()
         if new == 'm':
            quakes = sort_by_mag(quakes)
            table_stuff(quakes)
         elif new == 't':
            quakes = sort_by_time(quakes)
            table_stuff(quakes)
         elif new == 'l':
            quakes = sort_by_long(quakes)
            table_stuff(quakes)
         elif new == 'a':
            quakes = sort_by_lat(quakes)
            table_stuff(quakes)
      elif ans == 'f' or ans == 'F':
         new = input("Filter by (m)agnitude or (p)lace? ")
         new = new.lower()
         if new == 'm':
            low = float(input("Lower bound: "))
            hi = float(input("Upper bound: "))
            print()
            table_stuff(filter_by_mag(quakes,low,hi))
         elif new == 'p':
            word = input("Search for what string? ")
            print()
            table_stuff(filter_by_place(quakes,word))
      elif ans == 'n' or ans == 'N':
         print()
         quakes_dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
         count = 0
         for val in range(quakes_dict["metadata"]["count"]):
            n_quake = quake_from_feature(quakes_dict["features"][val])
            if n_quake not in quakes:
               quakes.append(n_quake)
               count += 1
         if count > 0:
            print("New quakes found!!!")
            print()
         table_stuff(quakes)
      else:
         next_ans = 'q'

   write_back(quakes)










if __name__ == '__main__':
   main()
