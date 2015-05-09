import game_functions as gf
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

def choose_word(diff, easy, med, hard):
    '''Use the choice returned from intro() to choose a random word from the
    appropriate list'''
    if diff == "e":
        word = random.choice(easy)
        return word
    elif diff == "m":
        word = random.choice(med)
        return word
    else:
        word = random.choice(hard)
        return word


def main_regular():
    guesses = 8
    guessed_letters = []
    easy = easy_words(word_list)
    med = medium_words(word_list)
    hard = hard_words(word_list)
    diff = intro()
    the_word = choose_word(diff, easy, med, hard)

    print("Your word is {} letters long".format(len(the_word)))

    #Loop through guesses
    while guesses > 0 and gf.still_playing(the_word,guessed_letters):
        guess = gf.ask_letter(guessed_letters)
        guessed_letters.append(guess)

        if guess not in the_word:
            guesses -= 1
            print("{} is not in the word, guesses left: {}\n".format(guess, guesses))
        else:
            print("{} is in the word, guesses left: {}\n".format(guess,guesses))

        gf.display_word(guessed_letters,the_word)
        #print(the_word)

    if guesses == 0:
        print("You lose, the word was {}".format(the_word))
        gf.play_again()

    gf.play_again()

if __name__ == "__main__":
    main_regular()
