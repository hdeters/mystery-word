import random

difficulty = ""
guesses = 8
guessed_letters = []
word_list = []

with open("/usr/share/dict/words") as filename:
    for line in filename:
        word_list.append(line.strip().lower())

def easy_words(word_list):
    easy_word_list = []
    for word in word_list:
        if len(word) < 7:
            easy_word_list.append(word)
    return easy_word_list

def medium_words(word_list):
    medium_word_list = []
    for word in word_list:
        if len(word) > 5 and len(word) < 9:
            medium_word_list.append(word)
    return(medium_word_list)

def hard_words(word_list):
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return(hard_word_list)

def random_word(word_list):
    word = random.choice(word_list)
    return word

def intro():
    options = ["e","m","h"]
    choice = input("Do you want to play (E)asy, (M)edium, or (H)ard mode?: ").lower()
    if choice in options:
        return choice
    else:
        print("That's not a valid choice, type E, M, or H")
        return intro()

def choose_word(diff):
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

def show_status(guess, word, current_stat):
#    for guess in guesses:
        if guess in word:
            print("{} is in the word".format(guess))
            spots = [i for i, letter in enumerate(word) if letter == guess]
            for idx in spots:
                current_stat[idx] = guess + " "
                for i in current_stat:
                    print (i, end="")
                    return current_stat
        else:
            print("{} is not in the word, guesses left: {}".format(guess, guesses))
            for i in current_stat:
                print(i,end='')
    return current_stat

def still_playing(the_word,guesses):
    word_as_list = list(the_word)
    if all(x in guesses for x in word_as_list):
        print("You win!!")
        return False
    else:
        return True

easy_list = easy_words(word_list)
med_list = medium_words(word_list)
hard_list = hard_words(word_list)

diff = intro()
the_word = choose_word(diff)

print("Your word is {} letters long".format(len(the_word)))

#Create empty blanks
blanks = []
length = len(the_word)
while length > 0:
    blanks.append('_ ')
    length -= 1

#Loop through guesses
while guesses > 0 and still_playing(the_word,guessed_letters):
    guess = ask_letter(guessed_letters)
    guessed_letters.append(guess)

    if guess not in the_word:
        guesses -= 1

    show_status(guess,the_word,blanks)

    print(the_word)
