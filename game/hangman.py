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

def display_hangman(number_of_guesses):
    if number_of_guesses == 0:
        return """
 +---+
 |   |    
 0   |
/|\\  |
/ \\  |
     |
======
    """
    elif number_of_guesses == 1:
        return """
 +---+
 |   |    
 0   |
/|\\  |
/    |
     |
======
    """
    elif number_of_guesses == 2:
        return """
 +---+
 |   |    
 0   |
/|\\  |
     |
     |
======
    """
    elif number_of_guesses == 3:
        return """
 +---+
 |   |    
 0   |
/|   |
     |
     |
======
    """
    elif number_of_guesses == 4:
        return """
 +---+
 |   |    
 0   |
/    |
     |
     |
======
    """
    elif number_of_guesses == 5:
        return """
 +---+
 |   |    
 0   |
     |
     |
     |
======
    """
    elif number_of_guesses == 6:
        return """
 +---+
 |   |    
     |
     |
     |
     |
======
    """

def display_word_progress(word_progress):
    for item in word_progress:
        print(item, end=" ")
    print()

def display_num_of_chances_remaining(number_of_guesses):
    print(f"you have {number_of_guesses} chances remaining!")