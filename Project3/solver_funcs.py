def check_valid(puzzle, cages):
   if check_cages_valid(puzzle, cages)==False or check_columns_valid(puzzle)==False or check_rows_valid(puzzle) == False:
      return False
   else:
      return True

def check_cages_valid(puzzle, cages):
   for cage in range(len(cages)):
      amount = cages[cage][0]
      length_of_lst2 = cages[cage][1] + 2
      sum_all = 0
      for val in range(2,length_of_lst2):
         first_value = cages[cage][val]
         if first_value < 5:
            if puzzle[0][first_value] == 0 and sum_all >= amount:
               return False 
            sum_all += puzzle[0][first_value]
         elif first_value < 10:
            if puzzle[1][first_value-5] == 0 and sum_all >= amount:
               return False
            sum_all += puzzle[1][first_value-5]
         elif first_value < 15:
            if puzzle[2][first_value-10] == 0 and sum_all >= amount:
               return False
            sum_all += puzzle[2][first_value-10]
         elif first_value < 20:
            if puzzle[3][first_value-15] == 0 and sum_all >= amount:
               return False
            sum_all += puzzle[3][first_value-15]
         else:
            if puzzle[4][first_value-20] == 0 and sum_all >= amount:
               return False
            sum_all += puzzle[4][first_value-20]

      if sum_all != amount and puzzle[first_value//5][first_value%5] != 0:
         return False
   
   return True

def check_columns_valid(puzzle):
   for col in range(5):
      for val in range(5):
         col_val = puzzle[val][col]
         for count in range(val):
            if col_val == puzzle[count][col] and puzzle[count][col] != 0:
               return False

   return True

def check_rows_valid(puzzle):
   for row in range(5):
      for val in range(5):
         row_val = puzzle[row][val]
         for count in range(val):
            if row_val == puzzle[row][count] and puzzle[row][count] != 0:
               return False

   return True

