import random

word_list = []

with open("/usr/share/dict/words") as filename:
    '''Read in dictionary of words'''
    for line in filename:
        word_list.append(line.strip().lower())

def easy_words(word_list):
    '''Assign words less than 7 characters to easy_word_list'''
    easy_word_list = []
    for word in word_list:
        if len(word) <= 6:
            easy_word_list.append(word)
    return easy_word_list

def medium_words(word_list):
    '''Assign words between 6 and 8 characters to medium_word_list'''
    medium_word_list = []
    for word in word_list:
        if len(word) > 5 and len(word) < 9:
            medium_word_list.append(word)
    return(medium_word_list)

def hard_words(word_list):
    '''Assign words greater than 8 characters to easy_word_list'''
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return(hard_word_list)

def random_word(word_list):
    '''Choose a random word from the given list and return it'''
    word = random.choice(word_list)
    return word

def intro():
    '''Ask the user what mode they would like to play (easy, med, hard) and
    return the choice'''
    options = ["e","m","h"]
    choice = input("Do you want to play (E)asy, (M)edium, or (H)ard mode?: ").lower()
    if choice in options:
        return choice
    else:
        print("That's not a valid choice, type E, M, or H")
        return intro()

def choose_word(diff):
    '''Use the choice returned from intro() to choose a random word from the
    appropriate list'''
    if diff == "e":
        word = random_word(easy_list)
        return word
    elif diff == "m":
        word = random_word(med_list)
        return word
    else:
        word = random_word(hard_list)
        return word

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
        main()
    elif play == "n":
        quit()
    else:
        print("That's not a valid input, enter 'y' or 'n'")
        return play_again()


def main():
    guesses = 8
    guessed_letters = []
    diff = intro()
    the_word = choose_word(diff)

    print("Your word is {} letters long".format(len(the_word)))

    #Loop through guesses
    while guesses > 0 and still_playing(the_word,guessed_letters):
        guess = ask_letter(guessed_letters)
        guessed_letters.append(guess)

        if guess not in the_word:
            guesses -= 1
            print("{} is not in the word, guesses left: {}\n".format(guess, guesses))
        else:
            print("{} is in the word, guesses left: {}\n".format(guess,guesses))

        display_word(guessed_letters,the_word)
        #print(the_word)

    if guesses == 0:
        print("You lose, the word was {}".format(the_word))
        play_again()

    play_again()

if __name__ == "__main__":
    easy_list = easy_words(word_list)
    med_list = medium_words(word_list)
    hard_list = hard_words(word_list)
    main()
