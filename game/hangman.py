import random

words = ["beach", "squid", "laugh", "grapes", "ground"]

def select_random_word_from_words(words):
    return random.choice(words)

def guess_the_letter():
    return input("make a guess: ")

def get_index_of_guess(guess, word):
    index = 0
    for item in word:
        if guess != item:
            index += 1
        else:
            break

    return index