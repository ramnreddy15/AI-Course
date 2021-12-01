import sys; args = sys.argv[1:]
puzzles = open(args[0], "r").read().splitlines()
import time

# optional helper function
def select_unassigned_var(assignment, variables, neighbors):
   min = 100
   value = -1
   for i,j in enumerate(assignment):
    if j ==".":
        if len(variables[i]) < min:
            min = len(variables[i])
            value = i
   return value

# optional helper function
def ordered_domain(var_index, variables, q_table):
   pass

# optional helper function
def update_variables(value, var_index, assignment, variables, neighbors):
   variables = {k:vals[:] for k,vals in variables.items()}
   for pos in neighbors[var_index]:
    if value in variables[pos]:
        variables[pos].remove(value)
   return variables
      
def solve(puzzle, neighbors):
   # initialize_ds function is optional helper function. You can change this part. 
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   return recursive_backtracking(list(puzzle), variables, neighbors, q_table)

# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables, neighbors, q_table):
   var = select_unassigned_var(assignment, variables, neighbors)
   if var == -1:
        return "".join(str(i) for i in assignment)
   for value in variables[var]:
       if assignment[var] != value and value in variables[var]:
#          q_table[value] = q_table[value]+1
         assignment[var] = value
         result = recursive_backtracking(assignment,update_variables(value, var, assignment, variables,neighbors),neighbors, q_table)
         if result != None: return result
         assignment[var] = "."
   return None

def sudoku_csp(n=9):
  
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
#    arr = [[0,1,2,9,10,11,18,19,20],
#        [3,4,5,12,13,14,21,22,23],
#        [6,7,8,15,16,17,24,25,26],
#        [27,28,29,36,37,38,45,46,47],
#        [30,31,32,39,40,41,48,49,50],
#        [33,34,35,42,43,44,51,52,53],
#        [54,55,56,63,64,65,72,73,74],
#        [57,58,59,66,67,68,75,76,77],
#        [60,61,62,69,70,71,78,79,80]]
#    return arr + [[(i*n)+j for j in range(n)] for i in range(n)] + [[(j*n)+i for j in range(n)] for i in range(n)]

def sudoku_neighbors(csp_table): # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
   neighbors = {}
   for i in range(81):
    for table in csp_table:
        if i in table:
            for val in table:
                if i in neighbors.keys():
                    if val not in neighbors[i]:
                       neighbors[i].append(val)
                else:
                    neighbors[i] = [val]
   return neighbors

# Optional helper function
def initialize_ds(puzzle, neighbors):
   variables = {}
   q_table = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
   for i, j in enumerate(puzzle): #maybe check is valid here later
        if j!=".":
            variables[i] = [int(j)]
   for i, j in enumerate(puzzle): #maybe check is valid here later
        temp = [1,2,3,4,5,6,7,8,9]
        if j==".":
            for var in neighbors[i]:
                if puzzle[var] != ".":
                    tempV = int(puzzle[var])
                    if tempV in temp:
                        temp.remove(tempV)
            variables[i] = temp
#    for i in puzzle:
#     if i != ".":
#         q_table[i] = q_table[i]+1
   return variables, puzzle, q_table


# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   return 324 if solution.count(".")==0 else 0

def main():
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line+1, puzzle.rstrip()
      print ("{}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# Required comment: Your name, Period #, 2022
# Check the example below. You must change the line below before submission.
# Ram Reddy, Period 5, 2022