# Name: Ram Reddy
# Date: 09/22/2021

words = set()
for word in open("words.txt","r"):
    words.add(word[:-1])
    
def swap(word, switch, i):
    word = list(word)
    word[i] = switch
    return "".join(word)

#current is a 6-letter word
#Find all one letter parat word from curent and store them in adj_list
def generate_adjacents(current, word_list):
    adj_list = set()
    for i in range(len(current)):
        for j in "abcdefghijklmnopqrstuvwxyz":
            if j!=current[i] and swap(current, j, i) in word_list:
                adj_list.add(swap(current, j, i))
    return adj_list

def display_path(n, explored):  # key: current, value: parent
    l = []
    while explored[n] != "s":  # "s" is initial's parent
        l.append(n)
        n = explored[n]
    l.append(n)
    return l[::-1]

def BFS(start, end, word_dict):
   explored = {start:"s"}
   Q = []
   Q.append(start)
   while True:
      if len(Q) == 0:
         return ("No Solution")
      s = Q.pop(0)      
      if s == end:
         arr = display_path(s, explored)
         return arr, len(arr)
      for a in generate_adjacents(s, word_dict):
         if a not in explored.keys():
            Q.append(a)
            explored[a] = s
            
def recur(start, end, word_dict, explored, limit):
    if start==end:
        arr = display_path(start, explored)
        return arr, len(arr) 
    elif limit == 0: return "No Solution", "NS"
    else:
        isCutoff = False
        for a in generate_adjacents(start, word_dict):
            if a not in explored.keys():
                explored[a] = start
                result = recur(a, end, word_dict, { key : explored[key] for key in explored }, limit-1)
                if result[0] == "No Solution": 
                    isCutoff = True
                else:
                    return result
        if isCutoff:
            return "No Solution", "NS"   
        return "No Solution", "NS"

def DLS(start, end, word_dict, limit):
    explored = {start:"s"}
    return recur(start, end, word_dict, explored, limit-1)

def IDS(start, end, word_dict, limit):
    for i in range(1,limit+1):
        path, steps = DLS(start, end, word_dict, i)
        if path != "No Solution":
            return path, steps
    return "No Solution", "NS"

def exitGracefully(start, end, limit=5):
    if start not in words or len(start) != 6:
        return 1
    if end not in words or len(start)!=6:
        return 1
    if not isinstance(limit, int):
        return 1
    if limit < 1 or limit > 20:
        return 1;
    return 0        

def main():
    start = input("Type the starting word: ")
    end = input("Type the goal word: ")
    if exitGracefully(start, end):
        return
    path, steps = BFS(start,end,words)
    print(path)
    print("The number of steps:", steps)
    try:
        limit = int(input("Type the limit (1 - 20): "))
    except:
        return    
    start = input("Type the starting word: ")
    end = input("Type the goal word: ")
    if exitGracefully(start, end, limit):
        return
    path, steps = DLS(start, end, words, limit)
    if path != "No Solution":
        print("Path:", path)
        print("steps within",limit ,"limit:", steps)
    else:
        print(path)
    path, steps = IDS(start, end, words, limit)
    print("Shortest Path:", path)
    print("Steps:", steps)
    
if __name__ == '__main__':
    main()
