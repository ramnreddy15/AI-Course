# Name: Ram Reddy
# Date: 11/15/2021

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for nine in csp_table:
      if len(set([assignment[i] for i in nine])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   min = 100
   value = -1
   for i,j in enumerate(assignment):
    if j ==".":
        if len(variables[str(i)]) < min:
            min = len(variables[str(i)])
            value = i
   return value

def isValid(value, var_index, assignment, variables, csp_table):
   if assignment[var_index] == str(value) or int(value) not in variables[str(var_index)]:
    return False
#    for table in csp_table:
#         if var_index in table:
#             for i in table:
#                 if assignment[i] == value:
#                     return False
   return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   variables = {k:vals[:] for k,vals in variables.items()}
   for table in csp_table:
     if var_index in table:
         for i in table:
            if int(value) in variables[str(i)]:
                temp = variables[str(i)]
                temp.remove(int(value))
                if len(temp) == 0:
                    temp = []
                variables[str(i)] = temp
   return variables

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment, csp_table): return assignment
   var = select_unassigned_var(assignment, variables, csp_table)
   for value in ["1","2","3","4","5","6","7","8","9"]:
       if var == -1:
            return assignment
       if isValid(value, var, assignment, variables, csp_table):
         assignment = list(assignment)
         assignment[var] = value
         result = recursive_backtracking("".join(assignment),update_variables(value, var, assignment, variables,csp_table), csp_table)
         if result != None: return result
         assignment[var] = "."
   return None

def display(solution):
   str = ""
   str+= "---------------------"
   temp = ""
   for i, j in enumerate(solution):
        if i%9 == 0:
            str+=temp+"\n"
            temp = ""
            if i!=0 and i%27==0:
                str += "\n"
        if (i+1)%3==0:
            temp+=j+"  "
        else:
            temp+=j + " "
   str+=temp+"\n"+"---------------------"
   return str

def sudoku_csp():
   """
    ---------------------
    0 1 2  3 4 5  6 7 8  
    9 10 11  12 13 14  15 16 17  
    18 19 20  21 22 23  24 25 26  

    27 28 29  30 31 32  33 34 35  
    36 37 38  39 40 41  42 43 44  
    45 46 47  48 49 50  51 52 53  

    54 55 56  57 58 59  60 61 62  
    63 64 65  66 67 68  69 70 71  
    72 73 74  75 76 77  78 79 80  
    ---------------------
   """
   arr = [
       # Squares
       [0,1,2,9,10,11,18,19,20],
       [3,4,5,12,13,14,21,22,23],
       [6,7,8,15,16,17,24,25,26],
       [27,28,29,36,37,38,45,46,47],
       [30,31,32,39,40,41,48,49,50],
       [33,34,35,42,43,44,51,52,53],
       [54,55,56,63,64,65,72,73,74],
       [57,58,59,66,67,68,75,76,77],
       [60,61,62,69,70,71,78,79,80],
       # Rows
       [0,1,2,3,4,5,6,7,8],
       [9,10,11,12,13,14,15,16,17],
       [18,19,20,21,22,23,24,25,26],
       [27,28,29,30,31,32,33,34,35],
       [36,37,38,39,40,41,42,43,44],
       [45,46,47,48,49,50,51,52,53],
       [54,55,56,57,58,59,60,61,62],
       [63,64,65,66,67,68,69,70,71],
       [72,73,74,75,76,77,78,79,80],
       #Cols
       [0,9,18,27,36,45,54,63,72],
       [1,10,19,28,37,46,55,64,73],
       [2,11,20,29,38,47,56,65,74],
       [3,12,21,30,39,48,57,66,75],
       [4,13,22,31,40,49,58,67,76],
       [5,14,23,32,41,50,59,68,77],
       [6,15,24,33,42,51,60,69,78],
       [7,16,25,34,43,52,61,70,79],
       [8,17,26,35,44,53,62,71,80]
   ]
   return arr

def initial_variables(puzzle, csp_table):
   variables = {}
   for i, j in enumerate(puzzle): #maybe check is valid here later
        if j!=".":
            variables[str(i)] = [j]
   for i, j in enumerate(puzzle): #maybe check is valid here later
        temp = [1,2,3,4,5,6,7,8,9]
        if j==".":
            for part in csp_table:
                if i in part:
                    for var in part:
                        if puzzle[var] != "." and int(puzzle[var]) in temp:
                            temp.remove(int(puzzle[var]))
            variables[str(i)] = temp
   return variables

def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()
    
#After run the 3rd sample input:
# ----jGRASP exec: python sudoku_part_1_Kim_2020_2021.py
# Type a 81-char string:
#....8....27.....54.95...81...98.64...2.4.3.6...69.51...17...62.46.....38....9....
# Input state
# ---------------------
# . . . . 8 . . . .
# 2 7 . . . . . 5 4
# . 9 5 . . . 8 1 .
#
# . . 9 8 . 6 4 . .
# . 2 . 4 . 3 . 6 .
# . . 6 9 . 5 1 . .
#
# . 1 7 . . . 6 2 .
# 4 6 . . . . . 3 8
# . . . . 9 . . . .
# ---------------------
# solution
# ---------------------
# 1 3 4 5 8 7 2 9 6
# 2 7 8 1 6 9 3 5 4
# 6 9 5 2 3 4 8 1 7
#
# 3 5 9 8 1 6 4 7 2
# 8 2 1 4 7 3 5 6 9
# 7 4 6 9 2 5 1 8 3
#
# 9 1 7 3 4 8 6 2 5
# 4 6 2 7 5 1 9 3 8
# 5 8 3 6 9 2 7 4 1
# ---------------------