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



# import random


# def read_file(file_name):
#     file = open(file_name,'r')
#     return file.readlines()


# def get_user_input():
#     return input('Guess the missing letter: ')


# def ask_file_name():
#     file_name = input("Words file? [leave empty to use words.txt] : ")
#     if not file_name:
#         return 'short_words.txt'
#     return file_name


# def select_random_word(words):
#     random_index = random.randint(0, len(words)-1)
#     word = words[random_index].strip()
#     return word


# # TODO: Step 1 - update to randomly fill in one character of the word only
# def random_fill_word(word):
#     #create a list of empty spaces(denoted by underscore) which are multiplied by the length of that word.
#     random_fill_word = list("_"*len(word)) 
#     randomIndex = random.randint(0,len(word)-1)
#     random_fill_word[randomIndex] = word[randomIndex]#randomindex of the list = randomindex of the word
#     random_fill_word = "".join(random_fill_word)#this converts a list to a string.
#     return random_fill_word
        

# # TODO: Step 1 - update to check if character is one of the missing characters
# def is_missing_char(original_word, answer_word, char):

#     for x in range(len(original_word)):  #use for loop 
#         if original_word[x] == char and answer_word[x] == "_": #empty underscore
#             return True #if the missing character matches the one found in the original word, then we return true
#     return False
    


# # TODO: Step 1 - fill in missing char in word and return new more complete word
# def fill_in_char(original_word, answer_word, char):
#     #TODO
# #create a list of empty underscore, and in our case that will be answer_word
# #import string
#     answer_word = list(answer_word)
#     for x in range(len(original_word)):
#         if original_word[x] == char and answer_word[x] == "_":
#         # original_word[x]== char
#              answer_word[x]=char
#     return "".join(answer_word)


# def do_correct_answer(original_word, answer, guess):
#     answer = fill_in_char(original_word, answer, guess)
#     print(answer)
#     return answer


# # TODO: Step 4: update to use number of remaining guesses
# def do_wrong_answer(answer, number_guesses):
#     print('Wrong! Number of guesses left: '+str(number_guesses))
#     draw_figure(number_guesses)


# # TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
# def draw_figure(number_guesses):
    
    
#     if number_guesses ==4:
#         print(("""/----
# |
# |
# |
# |
# _______"""))
#     elif number_guesses ==3:
#         print("""/----
# |   0
# |
# |
# |
# _______""")

#     elif number_guesses ==2:
#         print(("""/----
# |   0
# |   |
# |   |
# |
# _______"""))

        
#     elif number_guesses ==1:
#         print(("""/----
# |    0
# |   /|\\
# |    |
# |
# _______"""))

#     elif number_guesses ==0:
#         print("""/----
# |   0
# |  /|\\
# |   |
# |  / \\
# _______""")

# # TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# # TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# # TODO: Step 4 - keep track of number of remaining guesses
# def run_game_loop(word, answer):
#     print("Guess the word: "+answer)
#     guesses=5
#     while  True:  
#         guess = get_user_input()

#         if guess.lower()=="exit" or guess.lower()=="quit": #if you decide to quit or exit, then it will break/won't continue.
#             print("Bye!")
#             break

#         if is_missing_char(word, answer, guess):
#             answer = do_correct_answer(word, answer, guess)
#             if answer==word: #if the user guessed the answer which is the same as the word in our list,
#                 break # we break, there is no need to continue
#         else:
#             guesses-=1 # as you guess, the number of guesses decrease by 1.
#             if guesses>0: #if your guesses are greater than zero, then youcan keep guessing the wrong answer
#                 do_wrong_answer(answer, guesses)
#             else:
#                 do_wrong_answer(answer, guesses)
#                 print("Sorry, you are out of guesses. The word was: "+word) #if you run out of guesses then you can print this statement. 
#                 break
            


# # TODO: Step 6 - update to get words_file to use from commandline argument
# if __name__ == "__main__":
#     words_file = ask_file_name()
#     words = read_file(words_file)
#     selected_word = select_random_word(words)
#     current_answer = random_fill_word(selected_word)

#     run_game_loop(selected_word, current_answer)

