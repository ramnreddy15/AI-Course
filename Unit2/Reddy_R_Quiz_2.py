# Name: Ram Reddy
# Date: 11/10/2021

def check_complete(arr):
   if len(arr) > 6:
       return True
   return False

def select_unassigned_var(arr):
   for value in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
    if value not in arr:
        return value
   
def isValid(value,arr,places):
   if(len(arr) == 0): return True
   if value in arr:
    return False
   for i in arr:
        if value in places[i]:
            return False
   return True
            

def backtracking_search(arr,places): 
   return recursive_backtracking(arr,places,[])

def recursive_backtracking(arr,places,sizes):
   if check_complete(arr): return arr
   for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
       var = i
       if isValid(var, arr,places):
         arr.append(var)
         result = recursive_backtracking(arr,places,sizes)
         if result != None and sum(result) not in sizes:
            sizes.append(sum(result))
            print("Independent Set is:",result, "Sum is:", sum(result))
         arr.remove(var)
   return None

def main(): 
   neighbors = {0:[1,10,19],1:[8,0,2],2:[1,3,6],3:[2,4,19],4:[3,5,17],5:[4,6,15],6:[2,5,7],7:[6,8,14],8:[1,9,7],9:[13,10,8],10:[0,11,9],11:[10,12,18],12:[11,13,16],13:[9,12,14],14:[7,13,15],15:[5,16,14],16:[12,15,17],17:[4,16,18],18:[11,17,19],19:[0,3,18]}
   for key in neighbors.keys():
       temp = neighbors
       backtracking_search([key],temp)

if __name__ == '__main__':
   main()
   