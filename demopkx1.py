class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

class Board:
    def __init__(self):
        self.board = [[' ' for j in range(3)] for i in range(3)]
        
    def display(self):
        for row in self.board:
            print("|".join(row))
            
    def update(self, row, col, symbol):
        self.board[row][col] = symbol
        
    def winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        
        return None

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
    def move(self, board):
        # Get player's move
        row, col = input("Enter your move (row col): ").split()
        row, col = int(row), int(col)
        
        # Update the board
        board.update(row, col, self.symbol)