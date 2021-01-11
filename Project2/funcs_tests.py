# Project 2 - Moonlander
#
# Name: James Plasko
# Instructor: Brian Jones
# Section: 21

import unittest
from lander_funcs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(update_acceleration(1.62, 0), -1.62)

   def test_update_acc2(self):
      self.assertEqual(update_acceleration(1.62, 5), 0)   

   def test_update_acc3(self):
      self.assertAlmostEqual(update_acceleration(1.62, 9), 1.296)

   def test_update_altitude1(self):
      self.assertAlmostEqual(update_altitude(130.6677, -1.62, -1.62), 128.2377)

   def test_update_altitude2(self):
      self.assertAlmostEqual(update_altitude(1300, -45.24, 1.296), 1255.408)

   def test_update_altitude3(self):
      self.assertAlmostEqual(update_altitude(123.42, 3.25, 2.45), 127.895)

   def test_update_velocity1(self):
      self.assertAlmostEqual(update_velocity(-23.543, 2.36), -21.183)

   def test_update_velocity2(self):
      self.assertAlmostEqual(update_velocity(2.49, -1.63), 0.86)

   def test_update_fuel1(self):
      self.assertEqual(update_fuel(500, 9), 491)

   def test_update_fuel2(self):
      self.assertEqual(update_fuel(4, 9), -5)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

