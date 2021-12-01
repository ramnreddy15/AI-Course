# Name: Ram Reddy
# Date: 11/10/2021

def check_complete(places):
   if 12 in places.values():
    return False
   keys = ["T","A","B","C","D"]
   dif = []
   for i in range(4):
    for j in range(i+1,5):
        temp = abs(places[keys[i]]- places[keys[j]])-1
        if temp not in dif:
            dif.append(temp)
        else:
            return False
   return True
   
def select_unassigned_var(places):
   for key in places.keys():
    if places[key] == 12:
        return key
   
def isValid(value,places):
   if value in places.values():
    return False
   keys = ["T","A","B","C","D"]
   dif = []
   for i in range(4):
    for j in range(i+1,len(keys)):
        if places[keys[i]] != 12 and places[keys[j]] != 12:
            temp = abs(places[keys[i]]- places[keys[j]]) -1
            dif.append(temp)
        
   for i in places:
    if(abs(places[i] - value)-1 in dif):
        return False
   return True
            

def backtracking_search(places): 
   return recursive_backtracking(places)

def recursive_backtracking(places):
   if check_complete(places): return places
   var = select_unassigned_var(places)
   for value in [1,2,3,4,5,6,7,8,9,10,11]:
       if isValid(value, places):
         places[var] = value
         result = recursive_backtracking(places)
         if result != None: print(result)
         places[var] = 12
   return None

def main(): 
   places = {"T":12,"A":12, "B":12,"C":12,"D":12}
   for key in ["T","A","B","C","D"]:
       for value in [0,1,2,3,4,5,6,7,8,9,10,11]:
           temp = places
           temp[key] = value
           print(backtracking_search(temp))

if __name__ == '__main__':
   main()
   