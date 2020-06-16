import numpy as np

class Dartboard():
    
    def __init__(self, size):
        self.board = np.zeros(shape=size)
        
        self.centre_pt = tuple((int(size[0]/2), int(size[1]/2)))  # y, x
    
    def printBoardSection(self, centre, r):
        y_low = 0
        if centre[0]-r > 0:
            y_low = centre[0]-r
        
        y_high = len(self.board)
        if centre[0]+r < len(self.board):
            y_high = centre[0]+r
        
        x_low = 0
        if centre[1]-r > 0:
            x_low = centre[1]-r
            
        x_high = len(self.board)
        if centre[1]+r < len(self.board):
            x_high = centre[1]+r
        
        for i in range(y_low, y_high):
            for j in range(x_low, x_high):
                if i == y_low + (y_high - y_low)/2 and j == x_low + (x_high - x_low)/2:
                    print('|' + str(int(board[i][j])).ljust(2), end='')
                else:
                    print(str(int(self.board[i][j])).ljust(3), end='')
            print()
    
    def graphBoard(self):
        pass