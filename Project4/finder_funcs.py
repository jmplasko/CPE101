def get_rows(puzzle_string):
   new_list = []
   inside_list = []
   for val in range(1,101):
      if val%10 == 0:
         inside_list.append(puzzle_string[val-1])
         new_list.append(inside_list)
         inside_list = []
      else:
         inside_list.append(puzzle_string[val-1])

   return new_list

def get_columns(puzzle_string):
   new_list = []
   for val in range(10):
      inside_list = []
      for yee in range(10):
         inside_list.append(puzzle_string[yee*10+val])
      new_list.append(inside_list)

   return new_list

def forward(word,puzzle_string):
   new_boi = get_rows(puzzle_string)
   for val in range(10):
      for let in range(10):
         if word[0] == new_boi[val][let]:
            lang = len(word)
            total = lang + let
            new_word = "".join(new_boi[val][let:total])
            if word == new_word:
               position = [1,val,let]
               return position
   return False

def backward(word,puzzle_string):
   new_boi = get_rows(puzzle_string)
   for val in range(10):
      for let in range(10):
         if word[0] == new_boi[val][let]:
            lang = len(word)
            total = let+1 - lang
            if total >= 0:
               new_word = "".join(new_boi[val][total:let+1])
               new_word = new_word[::-1]
               if word == new_word:
                  position = [2,val,let]
                  return position
   return False

def up(word,puzzle_string):
   new_boi = get_columns(puzzle_string)
   for val in range(10):
      for let in range(10):
         if word[0] == new_boi[val][let]:
            lang = len(word)
            total = let+1 - lang
            if total >= 0:
               new_word = "".join(new_boi[val][total:let+1])
               new_word = new_word[::-1]
               if word == new_word:
                  position = [3,let,val]
                  return position
   return False  

def down(word,puzzle_string):
   new_boi = get_columns(puzzle_string)
   for val in range(10):
      for let in range(10):
         if word[0] == new_boi[val][let]:
            lang = len(word)
            total = lang + let
            new_word = "".join(new_boi[val][let:total])
            if word == new_word:
               position = [4,let,val]
               return position
   return False


def check(word,puzzle_string):
   if down(word,puzzle_string) !=  False:
      return down(word,puzzle_string)
   elif up(word,puzzle_string) !=  False: 
      return up(word,puzzle_string)
   elif backward(word,puzzle_string) != False:
      return backward(word,puzzle_string)
   elif forward(word,puzzle_string) != False:
      return  forward(word,puzzle_string)
   
   return False

def print_stuff(words,puzzle_string):
   for val in words:
      answers = check(val,puzzle_string)
      if answers != False:
         if answers[0] == 1:
            print("{:s}: (FORWARD) row: {:d} column: {:d}".format(val,answers[1],answers[2]))
         elif answers[0] == 2:
            print("{:s}: (BACKWARD) row: {:d} column: {:d}".format(val,answers[1],answers[2]))
         elif answers[0] == 3:
            print("{:s}: (UP) row: {:d} column: {:d}".format(val,answers[1],answers[2]))
         elif answers[0] == 4:
            print("{:s}: (DOWN) row: {:d} column: {:d}".format(val,answers[1],answers[2]))
      else:
         print("{:s}: word not found".format(val))

def puzzle(puzzle_string):
   puzzle = get_rows(puzzle_string)
   for row in range(10):
      print("".join(puzzle[row][:10]))
