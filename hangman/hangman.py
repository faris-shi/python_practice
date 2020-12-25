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


def hangman(lives):
    word = get_random_word()
    word_letters = set(word) #all letters that use has not guessed correctly
    used_letters = set()   #what user has guessed
    alphabet = set(string.ascii_uppercase)

    while lives > 0 or (lives == -1 and len(word_letters) > 0):
        time.sleep(1)
        os.system('clear')

        sorted_used_letters = list(used_letters)
        sorted_used_letters.sort()
        print('You have guessed these letters:', ' '.join(sorted_used_letters))

        current_letters = [letter if letter in used_letters else '-' for letter in word]
        print('Current words: ', ' '.join(current_letters))

        letter = input('Please guess one letter: ').upper()
        if letter not in alphabet:
            print('Invalided character. Please try again.')
            continue
        
        if letter in used_letters:
            print('You have already guessed this character. Please try again.')
            continue

        if lives != -1:
            lives = lives - 1
            print("The left lives:", lives)

        used_letters.add(letter)
        if letter not in word_letters:
            print('You did not guess correctly. Please try again.')
            continue

        print("Got it.")
        word_letters.remove(letter)

    print("------------------------------------------")    
    if len(word_letters) > 0:
        print("The word:", word)
        print('You lost game.')
    else:
        print("The word:", word)
        print('Congratulation, you win!')


    

if __name__ == "__main__":
    hangman(5)
