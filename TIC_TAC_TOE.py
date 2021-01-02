import random
import math
import time
import os

#abstract player class
class Player:

    def select(self, game):
        pass


class HumanPlayer(Player):

    def select(self, game):
        while True:
            try:
                index = int(input('Please choose one available number: '))
                if game.is_selected(index):
                    raise ValueError
                return index
            except ValueError:
                print('Invalid value, try again please!')

class RandomComputerPlayer(Player):

    # here can do smarter
    def select(self, game):
        return random.choice(game.availble_spots()).index

class Spot:

    EMPTY_LETTER = ' '

    O_LETTER = 'O'

    X_LETTER = 'X'

    def __init__(self, index):
        self.index = index
        self.letter = Spot.EMPTY_LETTER

    def select(self, letter):
        self.letter = letter
    
    def is_selected(self):
        return self.letter != Spot.EMPTY_LETTER

    def __str__(self):
        return self.letter if self.is_selected() else str(self.index)

    def __eq__(self, other):
        return self.letter == other.letter

class TicTacToeGame:

    def __init__(self):
        self.board = [Spot(i) for i in range(9)]

    def availble_spots(self):
        return [spot for spot in self.board if not spot.is_selected()]

    def is_selected(self, index):
        return self.board[index].is_selected()

    def select(self, index, letter):
        self.board[index].select(letter)

    def is_win(self, index, letter):

        def all_same(sequence):
            return all([str(spot) == letter for spot in sequence])

        # check whether spots are same horizontally
        row = index // 3
        if all_same(self.board[row* 3:(row + 1) * 3]):
            return True

        # check whether spots are same vertically
        col = index % 3
        if all_same(self.board[col::3]):
            return True
        
        # check whether spots are same in diagonals[0, 4, 8] and [2, 4, 6]
        if index in range(0, 9, 4) and all_same(self.board[0::4]):
            return True
        if index in range(2, 7, 2) and all_same(self.board[2:7:2]):
            return True
        
        return False
    
    def __str__(self):
        output = ''
        for row in [[str(spot) for spot in self.board[i * 3: (i + 1) * 3]] for i in range(3)]:
            output += '| ' + ' | '.join(row) + ' |\n'
        return output


def play(game, x_player, o_player):
    current_letter = Spot.X_LETTER

    while True:
        print(game)
        availble_spots = game.availble_spots()
        if len(availble_spots) == 0:
            print('It is tie.')
            return
        
        index = x_player.select(game) if current_letter == Spot.X_LETTER else o_player.select(game)
        game.select(index, current_letter)
        if game.is_win(index, current_letter):
            print(current_letter, 'player is Winner.')
            return
        current_letter = Spot.O_LETTER if current_letter == Spot.X_LETTER else Spot.X_LETTER
        time.sleep(0.5)
        os.system('clear')


if __name__ == "__main__":
    game = TicTacToeGame()
    x_player = HumanPlayer()
    o_player = RandomComputerPlayer()

    play(game, x_player, o_player)
