import random

words = ["beach", "squid", "laugh", "grapes", "ground"]

def select_random_word_from_words(words):
    return random.choice(words)

def guess_the_letter():
    return input("make a guess: ")