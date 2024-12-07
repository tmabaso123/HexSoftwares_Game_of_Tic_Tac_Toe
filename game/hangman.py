import random

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()

def ask_file_name():
    file_name = input("Words file? [leave empty to use words.txt] : ")
    if not file_name:
        return 'words.txt'
    return file_name


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

def run_hangman():
    number_of_guesses = 6
    guess_history = []
    words_file = ask_file_name()
    words = read_file(words_file)
    word = select_random_word_from_words(words).strip()  # Strip newline characters
    word_progress = ["_"] * len(word)  # Match the length of the word dynamically

    while number_of_guesses > 0:
        display_word_progress(word_progress)
        print(display_hangman(number_of_guesses))
        guess = guess_the_letter()

        if guess not in guess_history and guess in word:
            for i, letter in enumerate(word):  # Update all occurrences of the guessed letter
                if letter == guess:
                    word_progress[i] = guess

            guessed_word = ''.join(word_progress)
            if guessed_word == word:  # Check if the word is complete
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



