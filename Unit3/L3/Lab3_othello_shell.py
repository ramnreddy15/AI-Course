# Name: Ram Reddy
# Date: 1/12/2022

import random

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      moves = self.find_moves(board, color)
      best_move = moves[random.randint(0,len(moves)-1)]
      flipped = self.find_flipped(board, best_move[0],best_move[1],color)
      for coords in flipped:
         board[coords[0]][coords[1]] = color
      if color == "#000000":
         return best_move, 0
      else:
         return best_move, 1

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      stones = 0
      for row in board:
         for col in row:
            if col == '.':
               stones +=1
      return stones

   def find_moves(self, board, color):
    # finds all possible moves
      pos = []
      for i in range(self.x_max):
         for j in range(self.y_max):
            if board[i][j] == '.':
               pos.append([i,j])
      moves = []
      for p in pos:
         for direction in self.directions:
            x = p[0] + direction[0]
            y = p[1] + direction[1]
            if x>=0 and x<self.x_max and y>=0 and y<self.y_max and board[x][y] == self.opposite_color[color]:
              while x>=0 and x<self.x_max and y>=0 and y<self.y_max:
                if board[x][y] == color:
                    x = p[0]
                    y = p[1]
                    moves.append([x,y])
                    x = 100
                elif board[x][y] == self.opposite_color[color]:
                    x = x + direction[0]
                    y = y + direction[1]
                else:
                    x = 100

      return moves

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      flipped = []
      for direction in self.directions:
            x1 = x + direction[0]
            y1 = y + direction[1]
            if x1>=0 and x1<self.x_max and y1>=0 and y1<self.y_max and board[x1][y1] == self.opposite_color[color]:
              print("here1")
              temp = []
              while x1>=0 and x1<self.x_max and y1>=0 and y1<self.y_max:
                if board[x1][y1] == color:
                    print("here")
                    for var in temp:
                        flipped.append(var)
                    x1 = 100
                elif board[x1][y1] == self.opposite_color[color]:
                    temp.append([x1,y1])
                    x1 = x1 + direction[0]
                    y1 = y1 + direction[1]
                else:
                    x1 = 100
      return flipped

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      moves = self.find_moves(board, color)
      best_move = moves[random.randint(0,len(moves)-1)]
      flipped = self.find_flipped(board, best_move[0],best_move[1],color)
      self.make_move(board, color, move, flipped)
      if color == "#000000":
         return best_move, 0
      else:
         return best_move, 1

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      stones = 0
      for row in board:
         for col in row:
            if col == '.':
               stones +=1
      return stones

   def find_moves(self, board, color):
    # finds all possible moves
      pos = []
      for i in range(self.x_max):
         for j in range(self.y_max):
            if board[i][j] == '.':
               pos.append([i,j])
      moves = []
      for p in pos:
         for direction in self.directions:
            x = p[0] + direction[0]
            y = p[1] + direction[1]
            if x>=0 and x<self.x_max and y>=0 and y<self.y_max and board[x][y] == self.opposite_color[color]:
              while x>=0 and x<self.x_max and y>=0 and y<self.y_max:
                if board[x][y] == color:
                    x = p[0]
                    y = p[1]
                    moves.append([x,y])
                    x = 100
                elif board[x][y] == self.opposite_color[color]:
                    x = x + direction[0]
                    y = y + direction[1]
                else:
                    x = 100

      return moves

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      flipped = []
      for direction in self.directions:
            x1 = x + direction[0]
            y1 = y + direction[1]
            if x1>=0 and x1<self.x_max and y1>=0 and y1<self.y_max and board[x1][y1] == self.opposite_color[color]:
              print("here1")
              temp = []
              while x1>=0 and x1<self.x_max and y1>=0 and y1<self.y_max:
                if board[x1][y1] == color:
                    print("here")
                    for var in temp:
                        flipped.append(var)
                    x1 = 100
                elif board[x1][y1] == self.opposite_color[color]:
                    temp.append([x1,y1])
                    x1 = x1 + direction[0]
                    y1 = y1 + direction[1]
                else:
                    x1 = 100
      return flipped

   def minimax(self, board, color, search_depth):
    # returns best "value"
      # return 1
      return self.best_strategy(self, board, color)

   def negamax(self, board, color, search_depth):
    # returns best "value"
      # return 1
      return self.best_strategy(self, board, color)
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      # pass
      return self.best_strategy(self, board, color)

   def make_key(self, board, color):
    # hashes the board
      # return 1
      return self.best_strategy(self, board, color)

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
    for coords in flipped:
         board[coords[0]][coords[1]] = color

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      return 1

   def score(self, board, color):
    # returns the score of the board 
      return 1
