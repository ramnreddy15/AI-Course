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
    print()
    l = l[::-1]
    for i in l:
        print(i, end="   ")
    print()
    print("\n\nThe shortest path length is :", len(l))
    return ""

def BFS(start, end, word_dict):

   explored = {start:"s"}
   Q = []
   Q.append(start)
   while True:
      if len(Q) == 0:
         return ("No Solution")
      s = Q.pop(0)      
      if s == end:
         return display_path(s, explored)
      for a in generate_adjacents(s, word_dict):
         if a not in explored.keys():
            Q.append(a)
            explored[a] = s
            
def recur(start, end, word_dict, explored, limit):
    new_explored = { key : explored[key] for key in explored }
    if start==end:
        return display_path(start, explored)
    elif limit == 0: return None
    else:
        isCutoff = False
        for a in generate_adjacents(start, word_dict):
            explored[a] = start
            result = recur(a, end, word_dict, new_explored, limit-1)
            if result == None: 
                isCutoff = True
            else:
                return result
        if isCutoff:
            return None
                
  
#   Q = []
#   Q.append(start)
#   if len(Q) == 0:
#      return ("No Solution")
#   s = Q.pop()      
#   if s == end:
#      return display_path(s, explored)
#   for a in generate_adjacents(s, word_dict):
#      if a not in explored.keys():
#         Q.append(a)
        

def DLS(start, end, word_dict, limit):
    explored = {start:"s"}
    return recur(start, end, word_dict, explored, limit-1)

    
def main():
    print(DLS("foiled","cooper",words,5))


if __name__ == '__main__':
    main()
