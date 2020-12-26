import random
from words import words
import string
import os
import time

def get_random_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_random_word()
    word_letters = set(word) #all letters that users have not guessed correctly
    used_letters = set()   #what user has guessed
    alphabet = set(string.ascii_uppercase)

    #run until all letters have been guessed.
    while len(word_letters) > 0:
        time.sleep(1)
        os.system('clear') # clear terminal

        sorted_used_letters = list(used_letters)
        sorted_used_letters.sort()
        print('You have guessed these letters:', ' '.join(sorted_used_letters))

        #display word which shows the guessed letters as normal, unguessed letters as '-'
        current_letters = [letter if letter in used_letters else '-' for letter in word]
        print('Current words: ', ' '.join(current_letters))

        letter = input('Please guess one letter: ').upper()
        if letter not in alphabet:
            print('Invalided character. Please try again.')
            continue
        
        if letter in used_letters:
            print('You have already guessed this character. Please try again.')
            continue

        used_letters.add(letter)
        if letter not in word_letters:
            print('You did not guess correctly. Please try again.')
            continue

        print("Got it.")
        word_letters.remove(letter)

    print("------------------------------------------")    
    print("The word:", word)
    if len(word_letters) > 0:
        print('You lost game.')
    else:
        print('Congratulation, you win!')


    

if __name__ == "__main__":
    hangman()
