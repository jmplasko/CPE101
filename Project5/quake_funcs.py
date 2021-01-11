from urllib.request import urlopen
from json import loads
from datetime import datetime
import math
from operator import attrgetter, itemgetter

# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
   """Function to get a JSON dictionary from a website.

   Args:
      url (str): The url from which to get the JSON

   Returns:
      A Python dictionary containing the information from the JSON object
   """
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)


def time_to_str(time):
   """Converts integer seconds since unix epoch to a string.

   Args:
      time (int): Unix time

   Returns:
      A nicely formated time string
   """
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


class Earthquake:
   """A class to model earthquakes.

   Attributes: 
      place(str): The place of Eathquake
      mag(int): The magnitude of Earthquake
      longitude(float): The longitude of Earthquake
      latitude(float): The latitude of Earthquake
      time(int): The time Eathquake took place
   """

   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self,other):
      return lol(self.time,other.time) and self.place == other.place and lol(self.mag,other.mag) and lol(self.longitude,other.longitude) and lol(self.latitude,other.latitude)

   def __repr__(self):
      return "({:.2f}){:>40s} at {:s} ({:8.3f}, {:.3f})".format(self.mag,self.place,time_to_str(self.time),self.longitude,self.latitude)


def read_quakes_from_file(filename):
   earthquake_data = open("{:s}".format(filename),"r")
   object_list = []

   for val in earthquake_data:
      new_list = []
      new_list = val.split(" ")
      place = " ".join(new_list[4:len(new_list)])
      place = place.rstrip("\n")
      quake = Earthquake(place, float(new_list[0]), float(new_list[1]),float(new_list[2]), int(new_list[3]))
      object_list.append(quake)

   earthquake_data.close()   
   return object_list

def write_back(quakes):
   back = open("quakes.txt","w")
   for val in quakes:
      back.write("{} {} {} {:d} {:s}\n".format(val.mag,val.longitude,val.latitude,val.time,val.place))


def table_stuff(quakes):
   print("Earthquakes:")
   print("------------")
   for val in quakes:
      p = repr(val)
      print(p)
   print()

def lol(val1, val2, epsilon = .00001):
      return abs(val1 - val2) < epsilon

def sort_by_mag(quakes):
   return sorted(quakes, key=attrgetter('mag'), reverse=True)

def sort_by_time(quakes):
   return sorted(quakes, key=attrgetter('time'), reverse=True)

def sort_by_long(quakes):
   return sorted(quakes, key=attrgetter('longitude'))

def sort_by_lat(quakes):
   return sorted(quakes, key=attrgetter('latitude'))

def filter_by_mag(quakes, low, high):
   new = []
   for val in quakes:
      if val.mag >= low and val.mag <= high:
         new.append(val)

   return new

def filter_by_place(quakes, word):
   new = []
   for val in quakes:
      if word in val.place.lower():
         new.append(val)
   return new

def quake_from_feature(feature):
   object_list = []
   new = feature["geometry"]["coordinates"]
   quake = Earthquake(feature["properties"]["place"], feature["properties"]["mag"], new[0], new[1], (feature["properties"]["time"])//1000)   

   return quake
