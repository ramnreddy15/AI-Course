# Name: Ram Reddy
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   if(len(vars) != len(assignment)):
      return False
   for node in assignment:
      if node in adjs:
         for adj in adjs[node]:
            if adj != node and assignment[adj] == assignment[node]:
               return False
   return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   for key in vars.keys():
      if key not in assignment:
         return key

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   if var in adjs:
      for adj in adjs[var]:
         if adj in assignment:
            if adj != var and assignment[adj] == value:
               return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   if check_complete(assignment, variables, adjs): return assignment
   var = select_unassigned_var(assignment, variables, adjs)
   for value in variables[var]:
      if isValid(value, var, assignment, variables, adjs):
         assignment[var] = value
         result = recursive_backtracking(assignment, variables, adjs, shapes, frame)
         draw_shape(shapes[var], frame, value)
         if result != None: return result
         draw_shape(shapes[var], frame, "white")
         del assignment[var]
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   temp = open("mcNodes.txt")
   for node in temp:
      regions.append(node[:-1])

   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   temp = open("mcEdges.txt")
   for node in temp:
      node1, node2 = node.split(" ")
      if node1 not in adjacents:
         adjacents[node1] = [node2[:-1]]
      else:
         tempL = adjacents[node1]
         tempL.append(node2[:-1])
         adjacents[node1] = tempL
      if node2[:-1] not in adjacents:
         adjacents[node2[:-1]] = [node1]
      else:
         tempL = adjacents[node2[:-1]]
         tempL.append(node1)
         adjacents[node2[:-1]] = tempL
   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''