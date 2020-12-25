'''
practice command-line inesweeper
@Author: Faris.shi
'''
import random
from enum import Enum
import os
import time

class SpotType(Enum):
    '''
    define a type that represent what a spot is (normal spot or bomb spot)
    '''
    NORMAL = 1
    BOMB = 2

class Spot:

    def __init__(self):
        self.spot_type = SpotType.NORMAL
        self.num_neighbour_bombs = 0
        self.is_dig = False

    def __str__(self):
        if not self.is_dig:
            return ' '
        if self.spot_type == SpotType.BOMB:
            return '*'
        return str(self.num_neighbour_bombs)

class Board:

    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.num_dug = 0
        self.board = self._make_new_board()
        self._assign_num_neighbour_bombs()

    def dig(self, row, col):            
        spot = self.board[row][col]
        if spot.spot_type == SpotType.BOMB:
            return False

        self.num_dug += 1
        spot.is_dig = True
        if spot.num_neighbour_bombs == 0:
            return True

        for r in range(row - 1, row + 1 + 1):
            for c in range(col - 1, col + 1 + 1):
                if r == row and c == col:
                    continue
                if r < 0 or r >= self.dim_size or c <0 or c >= self.dim_size:
                        continue
                if self.board[r][c].is_dig:
                    continue

                self.dig(r, c)
        return True
        
    def _make_new_board(self):
        board = [[Spot() for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        num_bombs = 0
        while num_bombs < self.num_bombs:
            row = random.choice(list(range(self.dim_size)))
            col = random.choice(list(range(self.dim_size)))

            if board[row][col].spot_type == SpotType.BOMB:
                continue
            num_bombs += 1
            board[row][col].spot_type = SpotType.BOMB
        return board

    def _assign_num_neighbour_bombs(self):

        def do_assignment(row, col):
            num_bombs = 0
            for r in range(row - 1, row + 1 + 1):
                for c in range(col - 1, col + 1 + 1):
                    if r == row and c == col:
                        continue
                    if r < 0 or r >= self.dim_size or c <0 or c >= self.dim_size:
                        continue
                    if self.board[r][c].spot_type == SpotType.NORMAL:
                        continue

                    num_bombs += 1
            return num_bombs

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col].spot_type == SpotType.BOMB:
                    continue

                self.board[row][col].num_neighbour_bombs = do_assignment(row, col)

    def __str__(self):
        lines = ' '
        
        for i in range(self.dim_size):
            lines += ' | %d'%i
        lines += ' |\n------------------------------------------\n'

        for row in range(self.dim_size):
            lines += str(row) + ' | '
            for col in range(self.dim_size):
                spot = self.board[row][col]
                lines += spot.__str__() + ' | '
            lines += '\n'
        lines += '------------------------------------------'
        return lines


def play(dim_size = 10, num_bombs = 10):
    board = Board(10, 10)
    result = True
    while True:
        print('Num of dug spots: ', board.num_dug)
        if board.num_dug >= dim_size ** 2 - num_bombs:
            break
        
        print(board)

        try:
            row = int(input('Please enter row: '))
            col = int(input('Please enter col: '))
            assert row >= 0 and row < dim_size
            assert col >= 0 and col < dim_size

            result = board.dig(row, col)
            if not result:
                break
        except ValueError:
            print('Invalid row or col. Try again!')
            continue
        except AssertionError:
            print('Out of Bound. Try again!')
            continue
        time.sleep(0.5)
        os.system('clear')

    if result:
        print('Congratulation, you win')
    else:
        print('Sorry, you lost')

if __name__ == '__main__':
    play()
