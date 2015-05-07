import random

difficulty = "normal"
word = "deters"
guesses = 8
word_list = word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]

#with open("/usr/share/dict/words") as filename:
#    for line in filename:
#        word_list.append(line.strip().lower())

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

def ask_letter():
    guess = input("What is your guess?: ").lower()
    if guess.isalpha():
        return guess
    else:
        print("That's not a valid guess, please guess again.")
        ask_letter()



print (medium_words(word_list))



easy_list = easy_words(word_list)
med_list = medium_words(word_list)
hard_list = hard_words(word_list)
guess = ask_letter()

#print (guess)
