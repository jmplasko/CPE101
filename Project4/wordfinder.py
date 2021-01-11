from finder_funcs import *

def main():

   puzzle_string = input()
   words = input().split(" ")
   print("Puzzle:")
   print()
   puzzle(puzzle_string)
   print()
   print_stuff(words,puzzle_string)

if __name__ == '__main__':
   main()
