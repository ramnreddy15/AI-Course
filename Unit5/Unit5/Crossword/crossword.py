import sys; args = sys.argv[1:]
# Ram Reddy
# 2/25/2022

#!/usr/bin/python
#re.sub
import re
import math


def wordToSquares(word, type, row, col):
    if len(word) == 0:
        return []
    if type.upper() == "H":
        return [(row,i,word[i-col]) for i in range(col,col+len(word))]
    else:
        return [(i,col,word[i-row]) for i in range(row,row+len(word))]
    
def goodPositions(board, i , j):
    row = len(board)
    col = len(board[0])
    regex = "\w{3}"
    if(col>j+2):
        match = "".join([board[i][j], board[i][j+1], board[i][j+2]])
        if None != re.match(regex,match): return True
    if(0<=j-2):
        match = "".join([board[i][j], board[i][j-1], board[i][j-2]])
        if None != re.match(regex,match): return True
    if(row>i+2):
        match = "".join([board[i][j], board[i+1][j], board[i+2][j]])
        if None != re.match(regex,match): return True
    if(0<=i-2):
        match = "".join([board[i][j], board[i-1][j], board[i-2][j]])
        if None != re.match(regex,match): return True
    if(0<=i-1 and row>i+1):
        match = "".join([board[i][j], board[i-1][j], board[i+1][j]])
        if None != re.match(regex,match): return True
    if(0<=j-1 and col>j+1):
        match = "".join([board[i][j], board[i][j-1], board[i][j+1]])
        if None != re.match(regex,match): return True
    return False

def goodBlockPosition(board, i , j, blocks, makerBoard):
    row = len(board)
    col = len(board[0])
    regex = "^([-\w]{3}|#..)$"
    good = []
    if(col>j+3):
        match = "".join([board[i][j+1], board[i][j+2], board[i][j+3]])
        if None == re.match(regex,match): 
            return False
        else:
            good.append("c")
    if(0<=j-3):
        match = "".join([board[i][j-1], board[i][j-2], board[i][j-3]])
        if None == re.match(regex,match): 
            return False
        else:
            good.append("c")
    if(row>i+3):
        match = "".join([board[i+1][j], board[i+2][j], board[i+3][j]])
        if None == re.match(regex,match): 
            return False
        else:
            good.append("r")
    if(0<=i-3):
        match = "".join([board[i-1][j], board[i-2][j], board[i-3][j]])
        if None == re.match(regex,match): 
            return False
        else:
            good.append("r")
            
    if (j==0 and i>0 and board[i-1][j]!="#") or (j==len(board[0])-1 and i>0 and board[i-1][j]!="#"): return False
    if(i>0 and j>0 and i<len(board)-1 and j<len(board[0])-1):
        if(board[i-1][j-1]=="#" and board[i-1][j] == "#" and board[i+1][j+1]=="#") or (board[i-1][j]=="#" and board[i-1][j+1] == "#" and board[i+1][j-1]=="#"): 
            return False
    if i>0 and j<len(board[0]):
        if (board[i][j-1]=="#" and board[i][j-2]=="#" and board[i-1][j-3]=="#") or (board[i+1][j-1]=="#" and board[i][j+1]=="#"): return False
    if i>0 and j==len(board[0])-3:
        if board[i][j+1] !="#" or board[i][j+2] != "#": return False 
    if i>0 and j==len(board[0])-2:
        if board[i][j+1] !="#": return False
    if i>=2 and board[i-1][j] =="-" and board[i-2][j] == "#": return False
    return True if ("r" in good and "c" in good) else False

def areaFill(board, r, c, places):
    if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] == "#" or board[r][c] == "1":
        return places
    if(board[r][c]!="#"):
        board[r][c]="1"
        places.append((r,c))
        areaFill(board, r+1, c, places)
        areaFill(board, r-1, c, places)
        areaFill(board, r, c+1, places)
        areaFill(board, r, c-1, places)
        return places 
    
def checkBoard(board, makerBoard, blockPositions, blocks):
    temp = blocks
    for j in range(len(makerBoard[0])):
        for i in range(len(makerBoard)):
            if(board[i][j] == "#"):
                temp-=1
    good = True
    badPositions = []
    areas = []
    for i in range(len(makerBoard)):
        for j in range(len(makerBoard[0])):
            if board[i][j] == "#":
                if i>0 and i<3 and (board[i-1][j] != "#" or (i==2 and board[i-2][j] != "#")):
                    if board[i-1][j] != "#":
                        board[i-1][j] = "#"
                        makerBoard[i-1][j] = "#"
                    if i==2 and board[i-2][j] != "#":
                        board[i-2][j] = "#"
                        makerBoard[i-2][j] = "#"       
                if j>0 and j<3 and (board[i][j-1] != "#" or (j==2 and board[i][j-2] != "#")):
                    if board[i][j-1] != "#":
                        board[i][j-1] = "#"
                        makerBoard[i][j-1] = "#"
                    if j==2 and board[i][j-2] != "#":
                        board[i][j-2] = "#"
                        makerBoard[i][j-2] = "#"  
                if (j==(math.floor(len(board[0])/2)-1) and board[i][j+1] != "#" and board[i][j+2] == "#") or (j==(math.floor(len(board[0])/2))-2 and board[i][j+1] != "#"  and board[i][j+3] == "#"):
                    if (j==(math.floor(len(board[0])/2)-1) and board[i][j+1] != "#") or (j==(math.floor(len(board[0])/2))-2 and (board[i][j+1] != "#")):
                        board[i][j+1] = "#"
                        makerBoard[i][j+1] = "#"
                        board[len(board)-i-1][len(board[0])-j-2] = "#"
                        makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-2] = "#"  
                if j<len(board[0])-3 and "-#"=="".join([board[i][j+1],board[i][j+2]]):
                    board[i][j+1] = "#"
                if i<len(board)-3 and "-#"=="".join([board[i+1][j],board[i+2][j]]):
                    board[i+1][j] = "#"
                    areas.append((i,j,"r"))
                if j<len(board[0])-4 and "--#"=="".join([board[i][j+1],board[i][j+2],board[i][j+3]]):
                    board[i][j+1] = "#"
                    board[i][j+2] = "#"
                    areas.append((i,j,"c"))
                if i<len(board)-4 and "--#"=="".join([board[i+1][j],board[i+2][j],board[i+3][j]]):
                    board[i+1][j] = "#"
                    board[i+2][j] = "#"
        for j in range(len(makerBoard[0])):
            for i in range(len(makerBoard)):
                if board[i][j] == "#":
                    board[len(board)-i-1][len(board[0])-j-1] = "#"
                    makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "#"                   
        for j in range(len(makerBoard[0])):
            for i in range(len(makerBoard)):
                if(board[i][j] == "#" and (i, j) not in blockPositions):
                    blockPositions.append((i,j))
                    blocks-=1
                if board[i][j] != "-" and board[i][j] != "#" and not goodPositions(board, i, j):
                    good = False
                    badPositions.append((i,j))
    for i in range(len(makerBoard)):
        for j in range(len(makerBoard[0])):
            if board[i][j]=="-" and i>0 and j>0 and i<len(board)-1 and j<len(board[0])-1 and board[i-1][j+1]=="#" and board[i][j+1] == "#" and board[i+1][j-1]=="#":
                areas.append((i,j,"w"))
    for i,j,type in areas:
        area1 = ""
        area2 = ""
        if type=="w":
            board[i][j] = "#"
            area1 = areaFill([row[:] for row in board],i+1,j+1,[])
            area2 = areaFill([row[:] for row in board],i-1,j-1,[])
            if len(area1)==len(area2): board[i][j] ="-"
        elif type=="r":
            area1 = areaFill([row[:] for row in board],i+1,j+1,[])
            area2 = areaFill([row[:] for row in board],i+1,j-1,[])
        else:
            area1 = areaFill([row[:] for row in board],i-1,j+1,[])
            area2 = areaFill([row[:] for row in board],i+1,j+1,[])
        if len(area1)!=0 and len(area2)!=0 and len(area1) != len(area2):
            if len(area1) > len(area2):
                if temp-(2*len(area2))>0:
                    for r,c, in area2:
                        board[r][c] = "#"
                else:
                    board[i][j] ="-"
            else:
                if temp-(2*len(area1))>0:
                    for r,c, in area1:
                        board[r][c] = "#"
                else:
                    board[i][j] ="-"
    for j in range(len(makerBoard[0])):
        for i in range(len(makerBoard)):
            if board[i][j] == "#":
                board[len(board)-i-1][len(board[0])-j-1] = "#"
                makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "#"                   
    for j in range(len(makerBoard[0])):
        for i in range(len(makerBoard)):
            if(board[i][j] == "#" and (i, j) not in blockPositions):
                blockPositions.append((i,j))
                blocks-=1
            if board[i][j] != "-" and board[i][j] != "#" and not goodPositions(board, i, j):
                good = False
                badPositions.append((i,j))
    if(blocks != 0):
        good = False
    return good, blockPositions, blocks, badPositions, makerBoard
    
def createBoard(matches):
    m = re.match(r"^(?P<height>\d+)x(?P<width>\d+)$",matches[0])
    rows, cols = int(m.group("height")), int(m.group("width"))
    blocks = int(matches[1])
    board = [["-" for i in range(0, cols)] for j in range(0, rows)]
    makerBoard = [["-" for i in range(0, cols)] for j in range(0, rows)]
    for word in matches[2:]:
        m = re.match(r"^(?P<type>[VHvh])(?P<row>\d+)x(?P<col>\d+)(?P<word>(\w|#)*)$",word)
        for tup in wordToSquares("#" if m.group("word")=="" else m.group("word"), m.group("type"), int(m.group("row")), int(m.group("col"))): #################add none value
            board[tup[0]][tup[1]] = tup[2].upper()
    if rows*cols == blocks:
        for i in range(rows):
            for j in range(cols):
                board[i][j] = "#"
    if rows%2==1 and cols%2 == 1 and rows*cols != blocks:
        if blocks%2==1:
            board[int(rows/2)][int(cols/2)] = "#"
            makerBoard[int(rows/2)][int(cols/2)] = "#"
    for j in range(len(makerBoard[0])):
        for i in range(len(makerBoard)):
            if(board[i][j] != "-" and board[i][j] != "#"):
                makerBoard[i][j] = "~"
                makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "~"
            if board[i][j] == "#":
                board[len(board)-i-1][len(board[0])-j-1] = "#"
                makerBoard[i][j] = "#"
                makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "#"                
    return board, makerBoard

def generateBadPositions(makerBoard):
    for i in range(len(makerBoard)):
        for j in range(len(makerBoard[0])):    
            if makerBoard[i][j] == "~":
                if j==0 or (j>=1 and makerBoard[i][j-1] == "#"):
                    if j < len(makerBoard[0])-1 and makerBoard[i][j+1] != "#": makerBoard[i][j+1] = "~"
                    if j+2<=len(makerBoard[0])-1: makerBoard[i][j+2] = "~"
                elif j==len(makerBoard[0])-1 or (j<len(makerBoard[0])-1 and makerBoard[i][j+1] == "#"):
                    if makerBoard[i][j-1] != "#": makerBoard[i][j-1] = "~"
                    if makerBoard[i][j-2] != "#": makerBoard[i][j-2] = "~"
                elif j==1 and (makerBoard[i][j-1]=="~" or makerBoard[i][j+1]=="-"):
                    if makerBoard[i][j+1] != "#": makerBoard[i][j+1] = "~"
                if i==0 or (i>=1 and makerBoard[i-1][j] == "#"):
                    if i+1<=len(makerBoard)-1 and makerBoard[i+1][j] == "-": makerBoard[i+1][j] = "~"
                    if i+2<=len(makerBoard)-1 and makerBoard[i+1][j] == "-": makerBoard[i+2][j] = "~"
                elif i==len(makerBoard)-1  or (i<len(makerBoard)-1 and makerBoard[i-1][j] == "#"):
                    if makerBoard[i-1][j] != "#": makerBoard[i-1][j] = "~"
                    if makerBoard[i-2][j] != "#": makerBoard[i-2][j] = "~"
            if j==len(makerBoard[0])-3 and makerBoard[i][j-1] == "#":
               if makerBoard[i][j] != "#": makerBoard[i][j] = "~"
               if makerBoard[i][j+1] != "#": makerBoard[i][j+1] = "~"
               if makerBoard[i][j+1] != "#": makerBoard[i][j+2] = "~"
            if i==len(makerBoard)-3 and makerBoard[i-1][j] == "#":
                if makerBoard[i][j] != "#": makerBoard[i][j] = "~"
                if makerBoard[i+1][j] != "#": makerBoard[i+1][j] = "~"
                if makerBoard[i+2][j] != "#": makerBoard[i+2][j] = "~"
            
    for j in range(len(makerBoard[0])):
        for i in range(len(makerBoard)):
            if(makerBoard[i][j] == "~"):
                makerBoard[i][j] = "~"
                makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "~"
    return makerBoard

def makeGood(board, makerBoard, blockPositions, blocks, badPositions):
    reset = 1
    while(blocks != 0):
        for i in range(len(board)):
            for j in range(len(board[0])):
                generateBadPositions(makerBoard)        
                if j>0 and makerBoard[i][j-1]=="#" and (makerBoard[i][j] == "~" or makerBoard[i][j] == "-") and i==0 and j==len(board[0])-3 and blocks >= 6:
                    for c in range(3):
                        board[i][j+c] = "#"
                        board[len(board)-i-1][len(board[0])-j-1-c] = "#"
                        makerBoard[i][j+c] = "#"
                        makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1-c] = "#"  
                    blocks-=6
                    reset = 0
                elif makerBoard[i][j] == "-" and goodBlockPosition(board, i, j, blocks, makerBoard):
                    reset = 0
                    board[i][j] = "#"
                    board[len(board)-i-1][len(board[0])-j-1] = "#"
                    makerBoard[i][j] = "#"
                    makerBoard[len(makerBoard)-i-1][len(makerBoard[0])-j-1] = "#"  
                    blocks-=2
                if blocks == 0 or reset == 0:
                    break
            if blocks == 0 or reset == 0:
                reset = 1
                break
    return board, makerBoard
        
    
def main():
    matches = []
    matches2 = []
    board = []
    for i in range(len(args)):  
        temp = re.match(r"^\d+x\d+$", args[i])
        if temp != None:
            matches.append(temp[0]==args[i])
            matches2.append(temp[0])
        temp = re.match(r"^\d+$", args[i])
        if temp != None:
            matches.append(temp[0]==args[i])
            matches2.append(temp[0])
            
    for i in args[2:]:
        temp = re.match(r"^[HVhv]\d+x\d+.*$",i)
        matches.append(temp[0]==i)
        matches2.append(temp[0])
    if len(args[:]) == sum(matches):
        board, makerBoard = createBoard(matches2)
        good, blockPositions, blocks, badPositions, makerBoard = checkBoard(board, makerBoard, [], int(matches2[1]))

        if not good:
            board, makerBoard = makeGood(board, makerBoard, blockPositions, blocks, badPositions)
        for i in board:
            for j in i:
                print(j, end=" ")
            print()
    

if __name__ == "__main__":
    main()
    
# Ram Reddy, 5, 2023