# Name: Ram Reddy
# Date: 10/05/2021

import time

def generate_adjacents(current, words_set):
    ''' words_set is a set which has all words.
    By comparing current and words in the words_set,
    generate adjacents set of current and return it'''
    adj_set = set()
    for i in range(len(current)):
        for j in "abcdefghijklmnopqrstuvwxyz":
            if j != current[i] and swap(current, j, i) in words_set:
                current = list(current)
                current[j] = i
                adj_set.add("".join(word))
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

def dist_heuristic(state, goal="_123456789ABCDEF", size=4):
    total = 0
    for i in range(1, len(goal)):           
        temp = goal.find(state[i])
        total += abs(temp//size - i//size) + abs(temp % size - i % size)
    return total

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, word_set):
    explored = set(start)
    frontier = HeapPriorityQueue()
    frontier.push((heuristic(start, goal, size), start, [start]))
    while True:
        path = frontier.pop()
        s = path[1]
        path = path[2]
        if s == goal:
            return path
        for a in generate_adjacents(s,):
            length = len(path) + 1
            if not a in path:
                explored.add(a)
                frontier.push((heuristic(a, goal, size)+length, a, path+[a]))  


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
    path = (bi_bfs(initial, goal, words_set))
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
