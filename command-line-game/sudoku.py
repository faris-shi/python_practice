import random

class Block:

    EMPTY_NUMBER = -1

    def __init__(self):
        self.number = Block.EMPTY_NUMBER
        self.is_mask = False
        self.guess_number = Block.EMPTY_NUMBER
    
    def is_empty(self):
        if self.number == Block.EMPTY_NUMBER:
            return True
        return self.is_mask and self.guess_number == Block.EMPTY_NUMBER

    def value(self):
        return self.guess_number if self.is_mask else self.number

    def value_for_print(self):
        value = self.value()
        return " " if value == Block.EMPTY_NUMBER else str(value)

    def __eq__(self, number):
        if self.is_mask:
            return self.guess_number == number
        return self.number == number


class Sudoku:

    MAX_LENGTH = 9

    def __init__(self):
        self.puzzle = self._build_empty_puzzle()
        

    def _build_empty_puzzle(self):
        '''
        build 9 * 9 initial blocks
        '''
        puzzle = []
        for _ in range(Sudoku.MAX_LENGTH):
            puzzle.append([Block() for _ in range(Sudoku.MAX_LENGTH)])
        return puzzle

    def _is_valid(self, guess_number, row, col):
        '''
        check if the guess_number meets the row
        return True if meets, otherwise False
        '''
        # check number is in 3 * 3 section area 
        row_section_start = row // 3 * 3
        col_section_start = col // 3 * 3
        for i in range(row_section_start, row_section_start + 3):
            for j in range(col_section_start, col_section_start + 3):
                if self.puzzle[i][j] == guess_number:
                    return False

        # check if number is in horizontal line
        horizontal_array = [x.value() for x in self.puzzle[row]]
        if guess_number in horizontal_array:
            return False

        # check if number is in vertical line 
        vertical_array = [self.puzzle[i][col].value() for i in range(Sudoku.MAX_LENGTH)]
        if guess_number in vertical_array:
            return False

        return True

    def build(self):
        '''
        build random sudoku matrix by using backtracking
        '''
        def do_build(row = 0, col = 0):
            if row == Sudoku.MAX_LENGTH:
                return True

            if col == Sudoku.MAX_LENGTH:
                return do_build(row + 1, 0)

            single_list = list(range(1, 10))
            random.shuffle(single_list)

            for guess_number in single_list:
                if self._is_valid(guess_number, row, col):
                    self.puzzle[row][col].number = guess_number

                    if do_build(row, col + 1):
                        return True
                    self.puzzle[row][col].number = -1
            return False
        do_build()

    def mask(self, number=37):
        if number > Sudoku.MAX_LENGTH *  Sudoku.MAX_LENGTH:
            number = Sudoku.MAX_LENGTH * Sudoku.MAX_LENGTH

        for row in range(Sudoku.MAX_LENGTH):
            mask_number_in_row = random.randint(0, 8)

            if (Sudoku.MAX_LENGTH - row) * Sudoku.MAX_LENGTH >= number:
                mask_number_in_row = Sudoku.MAX_LENGTH

            mask_number_in_row = number if number < mask_number_in_row else mask_number_in_row

            random_col_index = random.sample(list(range(Sudoku.MAX_LENGTH)), mask_number_in_row)
            for col in random_col_index:
                self.puzzle[row][col].is_mask = True
            number -= mask_number_in_row


    def solve(self):
        def do_solve(row = 0, col = 0):
            if row == Sudoku.MAX_LENGTH:
                return True
            
            if col == Sudoku.MAX_LENGTH:
                return do_solve(row + 1, 0)

            if not self.puzzle[row][col].is_empty():
                return do_solve(row, col + 1)

            for guess_number in range(1, 10):
                if self._is_valid(guess_number, row, col):
                    self.puzzle[row][col].guess_number = guess_number

                    if do_solve(row, col + 1):
                        return True
                    self.puzzle[row][col].guess_number = -1
            return False 
        do_solve()

    
    def __str__(self):
        output = ""
        for row in range(Sudoku.MAX_LENGTH):
            if row % 3 == 0:
                output += " -----------------------\n"
            for col in range(9):
                if col % 3 == 0:
                    output += "| "
                output += self.puzzle[row][col].value_for_print() + " "
            output += "|\n"
        output += " -----------------------\n"
        return output


sudoku = Sudoku()
sudoku.build()
sudoku.mask(1)
print(sudoku)
sudoku.solve()
print(sudoku)