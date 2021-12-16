import sys

def game_over(board):
    if "." in board:
        if board[0] == "X":
            if board[4] == "X" and board[8] == "X":
                return True
        if board[0] == "O":
            if board[4] == "O" and board[8] == "O":
                return True
        if board[2] == "X":
            if board[4] == "X" and board[6] == "X":
                return True
        if board[2] == "O":
            if board[4] == "O" and board[6] == "O":
                return True
        for i in range(3):
            if board[i] == "X":
                if board[i+3] == "X" and board[i+6] == "X":
                    return True
            if board[i] == "O":
                if board[i+3] == "O" and board[i+6] == "O":
                    return True
        for i in range(0, 3, 3):
            if board[i] == "X":
                if board[i+1] == "X" and board[i+2] == "X":
                    return True
            if board[i] == "O":
                if board[i+1] == "O" and board[i+2] == "O":
                    return True
        if board[0] == "O":
            if board[4] == "O" and board[8] == "O":
                return True
        if board[2] == "O":
            if board[4] == "O" and board[6] == "O":
                return True
        if board[0:3] == "OOO" or board[3:6] == "OOO" or board[6:] == "OOO":
            return True
        for i in range(3):
            if board[i] == "O":
                if board[i+3] == "O" and board[i+6] == "O":
                    return True
        if board[0] == "X":
            if board[4] == "X" and board[8] == "X":
                return True
        if board[2] == "X":
            if board[4] == "X" and board[6] == "X":
                return True
        if board[0:3] == "XXX" or board[3:6] == "XXX" or board[6:] == "XXX":
            return True
        for i in range(3):
            if board[i] == "X":
                if board[i+3] == "X" and board[i+6] == "X":
                    return True
    else:
        return True
    return False

def Xwins(board):
    if board[0] == "X":
        if board[4] == "X" and board[8] == "X":
            return True
    if board[2] == "X":
        if board[4] == "X" and board[6] == "X":
            return True
    if board[0:3] == "XXX" or board[3:6] == "XXX" or board[6:] == "XXX":
        return True
    for i in range(3):
        if board[i] == "X":
            if board[i+3] == "X" and board[i+6] == "X":
                return True
    return False

def Owins(board):
    if board[0] == "O":
        if board[4] == "O" and board[8] == "O":
            return True
    if board[2] == "O":
        if board[4] == "O" and board[6] == "O":
            return True
    if board[0:3] == "OOO" or board[3:6] == "OOO" or board[6:] == "OOO":
        return True
    for i in range(3):
        if board[i] == "O":
            if board[i+3] == "O" and board[i+6] == "O":
                return True
    return False

def possible_next_boards(board, curplay):
    r = []
    for i in range(len(board)):
        if board[i] == ".":
            new_board = board[0:i] + curplay + board[i+1:]
            r.append((new_board, i))
    return r

def findcurrentplayer(board):
    numX = 0
    numO = 0
    for i in range(len(board)):
        if board[i] == "X":
            numX+=1
        if board[i] == "O":
            numO += 1
    if numO == numX:
        return "X"
    else:
        return "O"

def max_step(board):
    if game_over(board):
        if Xwins(board):
            return 1
        elif Owins(board):
            return -1
        else:
            return 0
    results = []
    current_player = findcurrentplayer(board)
    #print(board, possible_next_boards(board, current_player))
    for next_board in possible_next_boards(board, current_player):
        results.append(min_step(next_board[0]))
    #print(results)
    return max(results)
def max_move(board):
    results = []
    current_player = findcurrentplayer(board)
    #print(board, possible_next_boards(board, current_player))
    for next_board in possible_next_boards(board, current_player):
        results.append((min_step(next_board[0]), next_board[0], next_board[1]))
    #print(results)
    return (results)

def min_step(board):
    if game_over(board):
        if Xwins(board):
            return 1
        elif Owins(board):
            return -1
        else:
            return 0
    results = []
    current_player = findcurrentplayer(board)
    for next_board in possible_next_boards(board, current_player):
        results.append(max_step(next_board[0]))
    return min(results)

def min_move(board):
    results = []
    current_player = findcurrentplayer(board)
    for next_board in possible_next_boards(board, current_player):
        results.append((max_step(next_board[0]), next_board[0], next_board[1]))
    #print(results)
    return results



def displayboard(board):
    print('Current Board: ')
    print(board[0:3] + "     " + "012")
    print(board[3:6] + "     " + "345")
    print(board[6:] + "     " + "678")
    print()
def availablespaces(board):
    l = []
    for i in range(len(board)):
        if board[i] == ".":
            l.append(i)
    return l
board = sys.argv[1]
if board == ".........":
    player1 = input("Should I be X or O? ")
    displayboard(board)
    if player1 == "X":
        while(game_over(board) == False):
            l = availablespaces(board)
            r = max_move(board)
            
            for i in range(len(r)):
                v = ""
                if r[i][0] == 0:
                    v = "tie"
                elif r[i][0] == 1:
                    v = "win"
                else:
                    v = "loss"
                print("Moving at %s results in a %s" % (l[i], v))

            rv = max(r)
            print()
            print("I chose space %s" % rv[2])
            board = rv[1]
            print()
            displayboard(board)
            if(game_over(board)):
                break
            print("You can move to any of these spaces: %s" % availablespaces(board))
            chosenspace = int(input("Your Choice? "))
            board = board[0:chosenspace] + "O" + board[chosenspace+1:]
            print()
            displayboard(board)
        if(Owins(board)):
            print()
            print("You win")
        elif(Xwins(board)):
            print()
            print("I win")
        else:
            print()
            print("We tied")
    if player1 == "O":
        while(game_over(board) == False):
            print("You can move to any of these spaces: %s" % availablespaces(board))
            chosenspace = int(input("Your Choice? "))
            board = board[0:chosenspace] + "X" + board[chosenspace+1:]
            print()
            displayboard(board)
            if(game_over(board)):
                break
            l = availablespaces(board)
            r = min_move(board)
            
            for i in range(len(r)):
                v = ""
                if r[i][0] == 0:
                    v = "tie"
                elif r[i][0] == 1:
                    v = "loss"
                else:
                    v = "win"
                print("Moving at %s results in a %s" % (l[i], v))

            rv = min(r)
            print()
            print("I chose space %s" % rv[2])
            board = rv[1]
            print()
            displayboard(board)
        if(Owins(board)):
            print()
            print("I win")
        elif(Xwins(board)):
            print()
            print("You win")
        else:
            print()
            print("We tied")
else:
    player1 = findcurrentplayer(board)
    displayboard(board)
    if player1 == "X":
        while(game_over(board) == False):
            l = availablespaces(board)
            r = max_move(board)
            
            for i in range(len(r)):
                v = ""
                if r[i][0] == 0:
                    v = "tie"
                elif r[i][0] == 1:
                    v = "win"
                else:
                    v = "loss"
                print("Moving at %s results in a %s" % (l[i], v))

            rv = max(r)
            print()
            print("I chose space %s" % rv[2])
            board = rv[1]
            print()
            displayboard(board)
            if(game_over(board)):
                break
            print("You can move to any of these spaces: %s" % availablespaces(board))
            chosenspace = int(input("Your Choice? "))
            board = board[0:chosenspace] + "O" + board[chosenspace+1:]
            print()
            displayboard(board)
        if(Owins(board)):
            print()
            print("You win")
        elif(Xwins(board)):
            print()
            print("I win")
        else:
            print()
            print("We tied")
    if player1 == "O":
        while(game_over(board) == False):
            l = availablespaces(board)
            r = min_move(board)
            
            for i in range(len(r)):
                v = ""
                if r[i][0] == 0:
                    v = "tie"
                elif r[i][0] == 1:
                    v = "loss"
                else:
                    v = "win"
                print("Moving at %s results in a %s" % (l[i], v))

            rv = min(r)
            print()
            print("I chose space %s" % rv[2])
            board = rv[1]
            print()
            displayboard(board)
            if(game_over(board)):
                break
            print("You can move to any of these spaces: %s" % availablespaces(board))
            chosenspace = int(input("Your Choice? "))
            board = board[0:chosenspace] + "X" + board[chosenspace+1:]
            print()
            displayboard(board)
        if(Owins(board)):
            print()
            print("You win")
        elif(Xwins(board)):
            print()
            print("I win")
        else:
            print()
            print("We tied")