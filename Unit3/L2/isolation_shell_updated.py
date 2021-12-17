# Name: Ram Reddy
# Date: 12/10/2021
import random

class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      moves = self.find_moves(board,color)
      if(len(moves) == 0):
        return (-1,-1), 0
      # returns best move
      # (column num, row num), 0
      choice = list(moves)[random.randint(0,len(board)-1)]
      return (choice//5,choice%5), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
      print("here",board,color)
      moves = set()
      rowNum = 0
      if(self.first_turn):
        for col in board:
          for row in col:
            if(self.opposite_color[color] != self.black if row == "X" else self.white):
              moves.add(rowNum)
            rowNum +=1
        self.first_turn = False
      else:
        placeRow, placeCol, tempRow, tempCol = -1,0,0,0
        for col in board:
          for row in col:
            if(color != (self.black if row == "X" else self.white)):
              placeRow+=1
            if(color == (self.black if row == "X" else self.white)):
              placeRow+=1
              print(row)
              break
        placeCol = placeRow//5
        placeRow = placeRow%5
        placeRow-=1
        print(board[placeCol][placeRow])
        for way in self.directions:
          print(placeCol, placeRow)
          tempCol = placeCol
          tempRow = placeRow 
          while tempRow<5 and tempRow>=0 and tempCol<5 and tempCol>=0 and board[tempCol][tempRow] == ".":
            tempCol+=way[0]
            tempRow+=way[1]
            if tempRow<5 and tempRow>=0 and tempCol<5 and tempCol>=0 and board[tempCol][tempRow] == ".":
              moves.add(5*tempRow + tempCol)
      print(moves)
      return moves

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      return best_move, 0

   def minimax(self, board, color, search_depth):
      # search_depth: start from 2
      # returns best "value"
      return best_move, 1

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      return 1

   def find_moves(self, board, color):
      # finds all possible moves
      return set()

