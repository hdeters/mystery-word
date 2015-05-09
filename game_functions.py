from mystery_word import *
from demon_words import *

def intro_question():
    choice = input("Do you want to play (R)egular or (H)ard version?").lower()
    if choice == 'r':
        main_regular()
    elif choice == 'h':
        main_hard()
    else:
        print("Not a valid choice, enter R or H")
        return intro_question()

def display_word(guesses, word):
    '''Takes the list of guesses and the chosen word. Creates a list of blanks called
    current_stat that is the length of the chosen word. Checks if each guess is in the word.
    If true, assigns the guess to the correct index in current_stat.  Always puts
    previous guesses in current_stat as well as the new guess.'''
    current_stat = []
    length = len(word)
    while length > 0:
        current_stat.append("_ ")
        length -= 1
    for guess in guesses:
        if guess in word:
            spots = [i for i, letter in enumerate(word) if letter == guess]
            for idx in spots:
                current_stat[idx] = guess + " "
    for i in current_stat:
        print (i, end="")
    print("\n")

def ask_letter(guessed):
    '''Ask the user for a guess and make sure it is a letter and it is one letter.
    If it has not all ready been guessed, return the guess. Otherwise, ask for another
    guess'''
    guess = input("What is your guess?: ").lower()
    if guess.isalpha() and len(guess) == 1:
        if guess not in guessed:
            return guess
        else:
            print("You all ready guessed that letter!")
            return ask_letter(guessed)
    else:
        print("That's not a valid guess, please guess again.")
        return ask_letter(guessed)

def still_playing(the_word,guesses):
    '''checks if all of the letters in the chosen word are in guesses. If so,
    tell the user they won. If not, return true so the main while loop continues.'''
    word_as_list = list(the_word)
    if all(x in guesses for x in word_as_list):
        print("You win!!")
        return False
    else:
        return True


def play_again():
    '''Ask the user if they want to play again. Validate input'''
    play = input("Do you want to play again? (Y/N): ").lower()
    if play == "y":
        intro_question()
    elif play == "n":
        quit()
    else:
        print("That's not a valid input, enter 'y' or 'n'")
        return play_again()


if __name__ == "__main__":
    intro_question()
