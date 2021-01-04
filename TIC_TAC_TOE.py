import random
import math
import time
import os

#abstract player class
class Player:

    def __init__(self, letter):
        self.letter = letter

    def select(self, game):
        pass


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

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

    def __init__(self, letter):
        super().__init__(letter)

    def select(self, game):
        return random.choice(game.availble_spots()).index

class GeniusComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def select(self, game):

        # simulate all possibilities by using back-tracking algrithm.
        # here we wants to maximize the GeniuscomputerPlayer's score and minimize the other player's score.
        # so the formular is:
        # GeniuscomputerPlayer: 1 * (num_empyt_sponts + 1)
        # other_player: -1 * (num_empyt_sponts + 1)
        def minimax(state , player):
            other_player = Spot.O_LETTER if player == Spot.X_LETTER else Spot.X_LETTER

            # check the base case
            # check if the pervious player is the winner
            if state.current_winner == other_player:
                num_empty_spots = state.num_empty_spots()
                return {
                    "position": None,
                    # get score based on whether pervious player is the GeniuscomputerPlayer.
                    "score": 1 * (num_empty_spots + 1) if other_player == self.letter else -1 * (num_empty_spots + 1)
                }
            
            # if no any empty spots there, it is tie.
            if state.num_empty_spots == 0:
                return { "position": None, "score": 0}
            
            best = {
                "position": None,
                "score": -math.inf if player == self.letter else math.inf
            }

            for possible_move in state.availble_spots():
                #select any possible spot
                state.select(possible_move.index, player)
                #get score recursively
                sim_score = minimax(state, other_player)
                #cancel select
                state.un_select(possible_move.index)
                sim_score["position"] = possible_move.index
                
                if player == self.letter:
                    if best["score"] <= sim_score["score"]:
                        best = sim_score
                else:
                    if best["score"] >= sim_score["score"]:
                        best = sim_score 

            return best

        if len(game.availble_spots()) == 9:
            return random.choice(game.availble_spots()).index 
        
        best = minimax(game, self.letter)
        return best["position"]

class Spot:

    EMPTY_LETTER = ' '

    O_LETTER = 'O'

    X_LETTER = 'X'

    def __init__(self, index):
        self.index = index
        self.letter = Spot.EMPTY_LETTER

    def select(self, letter):
        self.letter = letter

    def un_select(self):
        self.letter = Spot.EMPTY_LETTER
    
    def is_selected(self):
        return self.letter != Spot.EMPTY_LETTER

    def __str__(self):
        return self.letter if self.is_selected() else str(self.index)

    def __eq__(self, other):
        return self.letter == other.letter

class TicTacToeGame:

    def __init__(self):
        self.board = [Spot(i) for i in range(9)]
        self.current_winner = Spot.EMPTY_LETTER

    def availble_spots(self):
        return [spot for spot in self.board if not spot.is_selected()]

    def num_empty_spots(self):
        return len(self.availble_spots())

    def is_selected(self, index):
        return self.board[index].is_selected()

    def select(self, index, letter):
        self.board[index].select(letter)
        if self.is_win(index, letter):
            self.current_winner = letter
    
    def un_select(self, index):
        self.board[index].un_select()
        self.current_winner = Spot.EMPTY_LETTER

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
        if game.num_empty_spots() == 0:
            print('It is tie.')
            return Spot.EMPTY_LETTER
        
        if game.current_winner != Spot.EMPTY_LETTER:
            print(game.current_winner, 'player is Winner.')
            return game.current_winner
        
        index = x_player.select(game) if current_letter == Spot.X_LETTER else o_player.select(game)
        game.select(index, current_letter)
 
        current_letter = Spot.O_LETTER if current_letter == Spot.X_LETTER else Spot.X_LETTER
        time.sleep(0.5)
        os.system('clear')
    
if __name__ == "__main__":
    game = TicTacToeGame()
    x_player = GeniusComputerPlayer(Spot.X_LETTER)
    o_player = RandomComputerPlayer(Spot.O_LETTER)

    play(game, x_player, o_player)
