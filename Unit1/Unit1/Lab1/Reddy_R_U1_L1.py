# Name: Ram Reddy
# Date: 09/17/2021

import random

GOAL_STRING = "_12345678"


def getInitialState():
    x = "_12345678"
    l = list(x)
    random.shuffle(l)
    y = ''.join(l)
    return "_42135678"


'''precondition: i<j
   swap characters at position i and j and return the new state'''


def swap(state, i, j):
    '''your code goes here'''
    temp = state[i]
    state = list(state)
    state[i] = state[j]
    state[j] = temp
    return "".join(state)


'''Generate a list which hold all children of the current state
   and return the list'''


def generate_children(state):
    size =3    
    blank = state.index('_')
    return [swap(state, blank, i) for i in [blank+1, blank-1, blank+size, blank-size] if i >= 0  and i < len(state)]



def display_path(n, explored):  # key: current, value: parent
    l = []
    while explored[n] != "s":  # "s" is initial's parent
        l.append(n)
        n = explored[n]
    print()
    l = l[::-1]
    for i in l:
        print(i[0:3], end="   ")
    print()
    for j in l:
        print(j[3:6], end="   ")
    print()
    for k in l:
        print(k[6:9], end="   ")
    print("\n\nThe shortest path length is :", len(l))
    return ""


'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


def BFS(initial_state):

   explored = {}
   explored[initial_state] = "s"
   Q = []
   Q.append(initial_state)
   while True:
      if len(Q) == 0:
         return ("No Solution")
      s = Q.pop(0)      
      if s == GOAL_STRING:
         return display_path(s, explored)
      for a in generate_children(s):
         if a not in explored.keys():
            Q.append(a)
            explored[a] = s


'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


def DFS(initial):
   explored = {}
   explored[initial] = "s"
   Q = []
   Q.append(initial)
   while True:
      if len(Q) == 0:
         return ("No Solution")
      s = Q.pop()      
      if s == GOAL_STRING:
         return display_path(s, explored)
      for a in generate_children(s):
         if a not in explored:
            Q.append(a)
            explored[a] = s


def main():
    initial = getInitialState()
    print("BFS start with:\n", initial[0:3],
          "\n", initial[3:6], "\n", initial[6:], "\n")
    print(BFS(initial))
    print("DFS start with:\n", initial[0:3],
          "\n", initial[3:6], "\n", initial[6:], "\n")
    print(DFS(initial))


if __name__ == '__main__':
    main()
