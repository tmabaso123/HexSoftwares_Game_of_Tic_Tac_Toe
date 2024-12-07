import random

def read_file(file_name):
    """
    Reads the contents of a file and returns a list of its lines.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of strings, where each string is a line from the file.
    """
    file = open(file_name,'r')
    return file.readlines()

def ask_file_name():
    """
    Prompts the user for a file name to read words from. 
    If no input is provided, defaults to 'words.txt'.

    Returns:
        str: The name of the file to use.
    """
    file_name = input("Words file? [leave empty to use words.txt] : ")
    if not file_name:
        return 'words.txt'
    return file_name


def select_random_word_from_words(words):
    """
    Selects a random word from a list of words.

    Args:
        words (list): A list of words.

    Returns:
        str: A randomly selected word from the list.
    """
    return random.choice(words)

def guess_the_letter():
    """
    Prompts the user to guess a letter.

    Returns:
        str: The letter guessed by the user.
    """
    return input("make a guess: ")

def get_index_of_guess(guess, word):
    """
    Finds the index of the first occurrence of a guessed letter in a word.

    Args:
        guess (str): The letter guessed by the user.
        word (str): The word being guessed.

    Returns:
        int: The index of the first occurrence of the guessed letter, 
        or the length of the word if the letter is not found.
    """
    index = 0
    for item in word:
        if guess != item:
            index += 1
        else:
            break

    return index

def display_hangman(number_of_guesses):
    """
    Displays the current hangman stage based on the number of remaining guesses.

    Args:
        number_of_guesses (int): The number of guesses left.

    Returns:
        str: A string representation of the hangman stage.
    """
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
    """
    Displays the current progress of the word being guessed.

    Args:
        word_progress (list): A list representing the guessed state of the word.
    """
    for item in word_progress:
        print(item, end=" ")
    print()

def display_num_of_chances_remaining(number_of_guesses):
    """
    Displays the number of chances remaining for the player.

    Args:
        number_of_guesses (int): The number of guesses left.
    """
    print(f"you have {number_of_guesses} chances remaining!")

def run_hangman():
    """
    Runs the Hangman game, allowing the user to guess letters until they either
    guess the word correctly or run out of chances.
    """
    number_of_guesses = 6
    guess_history = []
    words_file = ask_file_name()
    words = read_file(words_file)
    word = select_random_word_from_words(words).strip()  
    word_progress = ["_"] * len(word)  

    while number_of_guesses > 0:
        display_word_progress(word_progress)
        print(display_hangman(number_of_guesses))
        guess = guess_the_letter()

        if guess not in guess_history and guess in word:
            for i, letter in enumerate(word): 
                if letter == guess:
                    word_progress[i] = guess

            guessed_word = ''.join(word_progress)
            if guessed_word == word:  
                print(f"Congrats, you won! The word is {word.upper()}!")
                break

        elif guess not in word or (guess in guess_history and guess in word):
            number_of_guesses -= 1

        guess_history.append(guess)
        display_num_of_chances_remaining(number_of_guesses)

    if number_of_guesses == 0:
        print(display_hangman(number_of_guesses))
        print("Sorry, you failed. Hangman is dead.")
        print(f"The word was: {word.upper()}")
              

if __name__ == "__main__":
    print("WELCOME! YOU HAVE 6 CHANCES TO GUESS THE WORD!")
    print("_______________________________________________")
    run_hangman()


