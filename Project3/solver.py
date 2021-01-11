from solver_funcs import *

def main():
   puzzle = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
   cages = get_cages()
   backtrack = 0
   checks = 0
   puzzleSolved = False
   currentLocation = 0

   while puzzleSolved == False:
      if currentLocation <= 24:
         row = currentLocation // 5
         col = currentLocation % 5
         if puzzle[row][col] < 5:
            puzzle[row][col] += 1
            valid = check_valid(puzzle,cages)
            checks += 1
            if valid == True:
               currentLocation += 1
         else:
            puzzle[row][col] = 0
            currentLocation -= 1
            backtrack += 1
      else:
         puzzleSolved = True
   print()
   print("Solution:")
   print()
   for val in range(5):
      for num in range(5):
         if num == 4:
            print(puzzle[val][num],end="")
         else:
            print(puzzle[val][num],end=" ")
      print()
   print()
   print("checks: {:d} backtracks: {:d}".format(checks,backtrack))

def get_cages():
   cage_l = []
   cage_2 = []
   num_cag = int(input("Number of cages: "))

   for val in range(num_cag):
      valu = input("Cage number {:d}: ".format(val)).split(" ")

      for new in valu:
         cage_l.append(int(new))

      cage_2.append(cage_l)
      cage_l = []

   return cage_2

if __name__=='__main__':
   main()
