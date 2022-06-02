from collections import deque
import sys
import time

def print_puzzle(sz,board):
   for i in range(sz):
      for j in range(sz):
         if (j!=sz-1):
            print(board[sz*i+j]+" ",end="")
         else:
            print(board[sz*i+j],end="")
      print()

def find_goal(board):
   board=board.replace('.','')
   return "".join(sorted(board))+'.'

def get_children(board):
   dotLoc=board.find(".")
   bSz=int(len(board)**0.5)
   chiSt=[]
   if dotLoc//bSz>0:# Up
      tempB=board
      tempB=tempB[:dotLoc]+tempB[dotLoc-bSz]+tempB[dotLoc+1:]
      tempB=tempB[:dotLoc-bSz]+'.'+tempB[dotLoc-bSz+1:]
      chiSt.append(("Up",tempB))
   if dotLoc%bSz!=bSz-1:# Right
      tempB=board
      tempB=tempB[:dotLoc]+tempB[dotLoc+1]+tempB[dotLoc+1:]
      tempB=tempB[:dotLoc+1]+'.'+tempB[dotLoc+2:]
      chiSt.append(("Right",tempB))
   if dotLoc//bSz<bSz-1:# Down
      tempB=board
      tempB=tempB[:dotLoc]+tempB[dotLoc+bSz]+tempB[dotLoc+1:]
      tempB=tempB[:dotLoc+bSz]+'.'+tempB[dotLoc+bSz+1:]
      chiSt.append(("Down",tempB))
   if dotLoc%bSz!=0:# Left
      tempB=board
      tempB=tempB[:dotLoc]+tempB[dotLoc-1]+tempB[dotLoc+1:]
      tempB=tempB[:dotLoc-1]+'.'+tempB[dotLoc:]
      chiSt.append(("Left",tempB))
   return chiSt

def solvable(board):
   dotLoc=board.find(".")
   invCo=0
   for i in range(len(board)):
      if i==dotLoc:
         continue
      for j in range(i+1,len(board)):
         if j==dotLoc:
            continue
         if board[j]<board[i]:
            invCo+=1
   if len(board)%2==1:
      if invCo%2==0:
         return True
   else:
      if (invCo+dotLoc//(int(len(board)**0.5)))%2==1:
         return True
   return False

def goal_test(board):
   return board==find_goal(board)

def BFS_num_reachable(stBoard):
   fringe=deque()
   vis=set()
   fringe.append(stBoard)
   vis.add(stBoard)
   co=0
   while len(fringe)!=0:
      co+=1
      curBoard=fringe.popleft()
      for child in get_children(curBoard):
         if child[1] not in vis:
            fringe.append(child[1])
            vis.add(child[1])
   return co

def print_path(prevBoards,moves):
   for i in range(len(prevBoards)):
      print_puzzle(int(len(prevBoards[i])**0.5),prevBoards[i])
      print()
      if i!=len(prevBoards)-1:
         print(moves[i])

def print_path_rev(prevBoards,moves):
   for i in range(len(prevBoards)):
      print_puzzle(int(len(prevBoards[i])**0.5),prevBoards[i])
      print()
      if i!=len(prevBoards)-1:
         if moves[i]=="Up":
            print("Down")
         if moves[i]=="Right":
            print("Left")
         if moves[i]=="Down":
            print("Up")
         if moves[i]=="Left":
            print("Right")

def BFS_print_path(stBoard):
   goalBoard=find_goal(stBoard)
   fringe=deque()
   vis=set()
   fringe.append((stBoard,[stBoard],[]))
   vis.add(stBoard)
   while len(fringe)!=0:
      curBoard,prevBoards,moves=fringe.popleft()
      if curBoard==goalBoard:
         print(len(moves))
         print_path(prevBoards,moves)
         break
      for child in get_children(curBoard):
         if child[1] not in vis:
            fringe.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
            vis.add(child[1])

def BFS_hardest_3by3():
   stBoard="12345678."
   fringe=deque()
   vis=set()
   maxDist=0
   maxCo=0
   farState=[(stBoard,[stBoard],[])]
   fringe.append((stBoard,[stBoard],[]))
   vis.add(stBoard)
   while len(fringe)!=0:
      curBoard,prevBoards,moves=fringe.popleft()
      if len(moves)>maxDist:
         maxCo=1
         maxDist=len(moves)
         farState=[(curBoard,prevBoards,moves)]
      elif len(moves)==maxDist:
         maxCo+=1
         farState.append((curBoard,prevBoards,moves))
      for child in get_children(curBoard):
         if child[1] not in vis:
            fringe.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
            vis.add(child[1])
   i=1
   for farB in farState:
      print("Case:",i)
      print("Maximum steps needed:",maxDist)
      print_path_rev(farB[1][::-1],farB[2][::-1])
      i+=1

def BFS(stBoard):
   goalBoard=find_goal(stBoard)
   fringe=deque()
   vis=set()
   fringe.append((stBoard,[stBoard],[]))
   vis.add(stBoard)
   while len(fringe)!=0:
      curBoard,prevBoards,moves=fringe.popleft()
      if curBoard==goalBoard:
         return len(moves)
      for child in get_children(curBoard):
         if child[1] not in vis:
            fringe.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
            vis.add(child[1])

def BBFS(stBoard):
   goalBoard=find_goal(stBoard)
   fringeS=deque()
   visS={}
   fringeS.append((stBoard,0))
   visS[stBoard]=([stBoard])
   fringeG=deque()
   visG={}
   fringeG.append((goalBoard,[goalBoard],[]))
   visG[goalBoard]=([goalBoard],[])
   while len(fringeS)!=0 and len(fringeG)!=0:
      curBoard,prevBoards,moves=fringeS.popleft()
      if curBoard in visG:
         return(len(visS[curBoard][1])+len(visG[curBoard][1]))
      for child in get_children(curBoard):
         if child[1] not in visS:
            fringeS.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
            visS[child[1]]=(prevBoards+[child[1]],moves+[child[0]])
      curBoard,prevBoards,moves=fringeG.popleft()
      if curBoard in visS:
         return(len(visS[curBoard][1])+len(visG[curBoard][1]))
      for child in get_children(curBoard):
         if child[1] not in visG:
            fringeG.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
            visG[child[1]]=(prevBoards+[child[1]],moves+[child[0]])

def kDFS(stBoard,k):
   goalBoard=find_goal(stBoard)
   fringe=deque()
   vis=set()
   fringe.append((stBoard,[stBoard],[]))
   vis.add(stBoard)
   while len(fringe)!=0:
      curBoard,prevBoards,moves=fringe.pop()
      if curBoard==goalBoard:
         return curBoard
      if len(prevBoards)<=k:
         for child in get_children(curBoard):
            if child[1] not in vis:
               fringe.append((child[1],prevBoards+[child[1]],moves+[child[0]]))
               vis.add(child[1])
   return None

def IDDFS(stBoard):
   foundG=None
   k=1
   while foundG==None:
      foundG=kDFS(stBoard,k)
      k+=1
   return k
# print("1",BFS(".42135678"))  # N=3
# print("2",BFS("21345678."))
print("3",BBFS("4123C98BDA765.EF"))
print("4",BBFS("4123C98BDA765.FE"))