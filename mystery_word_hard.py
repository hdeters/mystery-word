from mystery_word import *
import random

#choice = input("Do you want to play regular or hard version?")

#if choice == 'e':
#    main()
#else:
#    print("hard version")

word_list = ["bird", "calf", "river", "iriri", "stream","begin","iowan","imide","igrii", "kneecap",  "cookbook",
              "language", "sneaker", "algorithm", "integration", "brain"]


#word_list = []
guess = "i"
word_length = 5

#with open("/usr/share/dict/words") as filename:
#    '''Read in dictionary of words'''
#    for line in filename:
#        word_list.append(line.strip().lower())

def find_initial_words(word_list,word_length):
    viable_words = []
    for word in word_list:
        if len(word) == word_length:
            viable_words.append(word)
    return viable_words

def is_guess_in_word(word_list,guess):
    yes_group = []
    no_group = []
    for word in word_list:
        if guess in word:
            yes_group.append(word)
        else:
            no_group.append(word)
    if yes_group > no_group:
        return yes_group, True
    else:
        return no_group, False

def sort_group(maxlen,sortlist):
    group = []
    for pair in sortlist:
        if len(pair[1]) == maxlen:
            group.append(pair)
    return group

def choose_new_group(yes_group):
    spots_dict = {}
    position_counts = {}
    word_groups = []

    for word in yes_group:
        spots = [i for i, letter in enumerate(word) if letter == guess]
        spots_dict[word] = spots

    sorted_positions = sorted(spots_dict.items(), key=lambda x:len(x[1]), reverse=True)
    #print(sorted_positions)

    first_pair = sorted_positions[0]
    maxlen = len(first_pair[1])
    while maxlen > 0:
        group = sort_group(maxlen,sorted_positions)
        word_groups.append(group)
        maxlen -= 1

    #print(word_groups)
    maxset = 0
    for set in word_groups:
        if len(set) > maxset:
            largest_group = set
            maxset = len(set)
    return largest_group

def choose_best_position(big_group):
    display_options = []
    sorted_group = sorted(big_group, key=lambda x:x[1], reverse=True)
    best_position = sorted_group[0]
    position = best_position[1]
    for group in sorted_group:
        if group[1] == position:
            display_options.append(group)
    return display_options

def display_the_word(word, guess):
    stuff = ""
    current_stat = []
    length = len(word[0])
    while length > 0:
        current_stat.append("_ ")
        length -= 1
    for idx in word[1]:
        current_stat[idx] = guess + " "
    for i in current_stat:
        stuff = stuff + i
        print (i, end="")
    print("\n")

def main():
    guessed_letters = []
    guesses = 3
    word_length = 5
    still_playing = True
    inGroup = False
    viable_words = find_initial_words(word_list,word_length)
    yes_group = is_guess_in_word(viable_words,guess)
    #print(yes_group)
    largest_group = choose_new_group(yes_group)
    display_options = choose_best_position(largest_group)
    #print(display_options)
    print_this = random.choice(display_options)
    print(print_this)


    while guesses > 0 and still_playing:
        working_word_list = is_guess_in_word(word_list,guess)
        guess = ask_letter(guessed_letters)
        guessed_letters.append(guess)
        working_group, inGroup = is_guess_in_word(display_options,guess)
        if inGroup:
            print("{} is in the word, guesses left:{}".format(guess,guesses))
        else:
            guesses -= 1
            print("{} is not in the word, guesses left:{}".format(guess,guesses))
        largest_group = choose_new_group(yes_group)
        display_options = choose_best_position(largest_group)
        print_this = random.choice(display_options)
        print(print_this)

        display_the_word(print_this, guess)


main()
