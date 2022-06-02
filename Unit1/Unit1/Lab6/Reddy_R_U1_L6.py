# Name: Ram Reddy
# Date: 10/05/2021

import time

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

def swap(word, switch, i):
    word = list(word)
    word[i] = switch
    return "".join(word)


def generate_adjacents(current, words_set):
    ''' words_set is a set which has all words.
    By comparing current and words in the words_set,
    generate adjacents set of current and return it'''
    adj_set = set()
    for i in range(len(current)):
        for j in "abcdefghijklmnopqrstuvwxyz":
            if j != current[i] and swap(current, j, i) in words_set:
                adj_set.add(swap(current, j, i))
    return adj_set


def check_adj(words_set):
    # This check method is written for words_6_longer.txt
    adj = generate_adjacents('listen', words_set)
    target = {'listee', 'listel', 'litten', 'lister', 'listed'}
    return (adj == target)

def display_path(n, explored):  # key: current, value: parent
    l = []
    while explored[n] != "s":  # "s" is initial's parent
        l.append(n)
        n = explored[n]
    l.append(n)
    return l[::-1]


def dist_heuristic(state, goal):
    total = 0
    for i in range(0, len(goal)):           
        if state[i] != goal[i]:
            total+=1
    return total

def a_star(start, goal, word_set):
    explored = set(start)
    frontier = HeapPriorityQueue()
    frontier.push((dist_heuristic(start, goal), start, [start]))
    while True:
        path = frontier.pop()
        s = path[1]
        path = path[2]
        if s == goal:
            return path
        for a in generate_adjacents(s,word_set):
            length = len(path) + 1
            if not a in explored:
                explored.add(a)
                frontier.push((dist_heuristic(a, goal)+length, a, path+[a]))  


def main():
    filename = input("Type the word file: ")
    words_set = set()
    file = open(filename, "r")
    for word in file.readlines():
        words_set.add(word.rstrip('\n'))
    print ("Check generate_adjacents():", check_adj(words_set))
    initial = input("Type the starting word: ")
    goal = input("Type the goal word: ")
    cur_time = time.time()
    path = (a_star(initial, goal, words_set))
    if path != None:
        print(path)
        print("The number of steps: ", len(path))
        print("Duration: ", time.time() - cur_time)
    else:
        print("There's no path")


if __name__ == '__main__':
    main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''
