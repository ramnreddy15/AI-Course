# Name: Ram Reddy
# Date: 09/29/2021

import random
import time
import math

class HeapPriorityQueue():

    def __init__(self):
        # we do not use index 0 for easy index calulation
        self.queue = ["dummy"]
        self.current = 1        # to make this object iterable

    def next(self):            # define what __next__ does
        if self.current >= len(self.queue):
            self.current = 1     # to restart iteration later
            raise StopIteration

        out = self.queue[self.current]
        self.current += 1

        return out

    def __iter__(self):
        return self

    __next__ = next

    def isEmpty(self):
        return len(self.queue) == 1    # b/c index 0 is dummy

    def swap(self, a, b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    # Add a value to the heap_pq
    def push(self, value):
        self.queue.append(value)
        self.heapUp(len(self.queue)-1)

    # helper method for push
    def heapUp(self, k):
        while((k+1) / 2 > 1):
            leftN = k//2
            rightN = (k - 1) // 2
            if (k % 2 != 0 and self.queue[k] < self.queue[rightN]):
                self.swap(k, rightN)
                k = rightN
            elif (k % 2 == 0 and self.queue[k] < self.queue[leftN]):
                self.swap(k, leftN)
                k = leftN
            else:
                k = 0

    # helper method for reheap and pop
    def heapDown(self, k, size):
        while ((2*k)+1 < size):
            leftN = 2*k
            rightN = (2*k)+1
            if self.queue[leftN] <= self.queue[rightN] and self.queue[leftN] < self.queue[k]:
                self.queue[k], self.queue[leftN] = self.queue[leftN], self.queue[k]
                k = leftN
            elif self.queue[leftN] > self.queue[rightN] and self.queue[rightN] < self.queue[k]:
                self.queue[k], self.queue[rightN] = self.queue[rightN], self.queue[k]
                k = rightN
            else:
                k = size

    # make the queue as a min-heap
    def reheap(self):
        for i in range(1, len(self.queue)):
            self.heapDown(i, len(self.queue))

    def pop(self):
        return self.remove(0)

    def remove(self, index):
        index = index + 1
        if (len(self.queue) > 1):
            temp = self.queue[index]
            self.queue[index] = self.queue[-1]
            self.queue.pop()
            self.heapDown(index, len(self.queue))
            return temp
        else:
            return None

def inversion_count(new_state, width=4, N=4):
    '''
    Depends on the size(width, N) of the puzzle,
    we can decide if the puzzle is solvable or not by counting inversions.
    If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
    If N is even, puzzle instance is solvable if
       the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
       the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
    '''
    loc= new_state.find("_")//width
    new_state = new_state.replace("_","")
    numInversions = 0
    for i in range(len(new_state)):
        for k in new_state[i+1:]:
            if new_state[i] > k:
                numInversions += 1
    if N % 2 == 1:
        return [False, True][numInversions % 2 == 0]
    else:
        if (loc % 2 == 0) and numInversions % 2 == 0:
            return True
        elif (loc % 2 == 1) and numInversions % 2 == 1:
            return True
    return False


def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
    sample_list = list(sample)
    random.shuffle(sample_list)
    new_state = ''.join(sample_list)
    while not inversion_count(new_state, size, size):
        random.shuffle(sample_list)
        new_state = ''.join(sample_list)
    return new_state


def swap(n, i, j):
    n = list(n)
    n[i], n[j] = n[j], n[i]
    return "".join(n) 


'''Generate a list which hold all children of the current state
   and return the list'''


def generate_children(state, size=4):
    blank = state.index('_')
    if blank%size == 0:
        return [swap(state, blank, i) for i in [blank+1, blank+size, blank-size] if i >= 0 and i < len(state)]
    if blank%size == size-1:
        return [swap(state, blank, i) for i in [blank-1, blank+size, blank-size] if i >= 0 and i < len(state)]
    return [swap(state, blank, i) for i in [blank+1, blank-1, blank+size, blank-size] if i >= 0 and i < len(state)]


def display_path(path_list, size):
    for n in range(size):
        for path in path_list:
            print(path[n*size:(n+1)*size], end=" "*size)
        print()
    print("\nThe shortest path length is :", len(path_list))
    return ""


''' You can make multiple heuristic functions '''


def dist_heuristic(state, goal="_123456789ABCDEF", size=4):
    total = 0
    for i in range(1, len(goal)):           
        temp = goal.find(state[i])
        total += abs(temp//size - i//size) + abs(temp % size - i % size)
    return total

def check_heuristic():
    a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
    b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
    return (a < b)

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size=4):
    explored = set(start)
    frontier = HeapPriorityQueue()
    frontier.push((heuristic(start, goal, size), start, [start]))
    while True:
        path = frontier.pop()
        s = path[1]
        path = path[2]
        if s == goal:
            return path
        for a in generate_children(s):
            length = len(path) + 1
            if not a in explored:
                explored.add(a)
                frontier.push((heuristic(a, goal, size)+length, a, path+[a]))                
                
def main():
    # A star
    print("Inversion works?:", check_inversion())
    print("Heuristic works?:", check_heuristic())
#     initial_state = getInitialState("_123456789ABCDEF", 4)
    initial_state = input("Type initial state: ")
    if inversion_count(initial_state):
        cur_time = time.time()
        path = (a_star(initial_state))
        if path != None:
#             print(path)
            display_path(path, 4)
        else:
            print("No Path Found.")
        print("Duration: ", (time.time() - cur_time))
    else:
        print("{} did not pass inversion test.".format(initial_state))


if __name__ == '__main__':
    main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''