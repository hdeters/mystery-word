import game_functions as gf
import random

#word_list = ["bird", "calf", "river", "iriri", "chime", "crank", "stream","begin","iowan","imide","igrii", "kneecap",  "cookbook",
#              "language", "sneaker", "algorithm", "integration", "brain"]

word_list = []
guess = ""

with open("/usr/share/dict/words") as filename:
    '''Read in dictionary of words'''
    for line in filename:
        word_list.append(line.strip().lower())

def get_length():
    the_length = input("How long do you want the word to be?: ")
    sorted_words = sorted(word_list, key=lambda x:len(x), reverse=True)
    max_word_length = len(sorted_words[0])
    try:
        length = int(the_length)
        if length <= max_word_length and length > 0:
            return length
        else:
            print("That length doesn't work, enter a number between 0 and {}".format(max_word_length))
            return get_length()
    except ValueError:
        print("Please enter a number")
        return get_length()

def get_guesses():
    guesses = input("How many guesses do you want?: ")
    try:
        the_guesses = int(guesses)
        return the_guesses
    except:
        print("Please enter a number")
        return get_guesses()

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
    if len(yes_group) > len(no_group):
        return yes_group, True
    else:
        return no_group, False

def sort_group(maxlen,sortlist):
    group = []
    for pair in sortlist:
        if len(pair[1]) == maxlen:
            group.append(pair)
    return group

def choose_new_group(working_group,guess):
    spots_dict = {}
    position_counts = {}
    word_groups = []

    for word in working_group:
        spots = [i for i, letter in enumerate(word) if letter == guess]
        spots_dict[word] = spots

    sorted_positions = sorted(spots_dict.items(), key=lambda x:len(x[1]), reverse=False)

    first_pair = sorted_positions[0]
    maxlen = len(first_pair[1])
    while maxlen > 0:
        group = sort_group(maxlen,sorted_positions)
        word_groups.append(group)
        maxlen -= 1

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

def ending(last_word,guessed_letters,guesses,guess):
    while guesses > 0:
        if gf.still_playing(last_word,guessed_letters):
            guess = gf.ask_letter(guessed_letters)
            guessed_letters.append(guess)
            if guess in last_word:
                print("{} is in the word, guesses left:{}".format(guess,guesses))
                gf.display_word(guessed_letters, last_word)
                return ending(last_word,guessed_letters,guesses,guess)
            else:
                guesses -= 1
                print("{} is not in the word, guesses left:{}".format(guess,guesses))
                gf.display_word(guessed_letters, last_word)
                return ending(last_word,guessed_letters,guesses,guess)
        else:
            return True
    return False

def create_blank_tuple(length):
    string = ""
    while length > 0:
        string = string + " "
        length -= 1
    blank_tup = (string,1)
    return blank_tup

def main_hard():
    guessed_letters = []
    word_length = get_length()
    guesses = get_guesses()
    in_word = False
    last_word = False
    print_this = create_blank_tuple(word_length)
    display_options = find_initial_words(word_list,word_length)

    while guesses > 0 and gf.still_playing(print_this,guessed_letters):

        if last_word:
            win = ending(the_word,guessed_letters,guesses,guess)
            if win:
                gf.play_again()
            else:
                print("You lose, the word was {}".format(the_word))
                gf.play_again()

        guess = gf.ask_letter(guessed_letters)
        working_group, in_word = is_guess_in_word(display_options,guess)

        if in_word:
            guessed_letters.append(guess)
            largest_group = choose_new_group(working_group,guess)
            display_tuples = choose_best_position(largest_group)
            print_this = random.choice(display_tuples)
            gf.display_word(guessed_letters, print_this[0])
            print("\n{} is in the word, guesses left:{}".format(guess,guesses))
            display_options = []
            for pair in display_tuples:
                display_options.append(pair[0])

        else:
            guesses -= 1
            gf.display_word(guessed_letters, print_this[0])
            print("\n{} is not in the word, guesses left:{}".format(guess,guesses))
            if len(working_group) == 1:
                last_word = True
                the_word = working_group[0]
            display_options = working_group
    print("You lose, the word was {}".format(random.choice(display_options)))
    gf.play_again()

if __name__ == "__main__":
    main_hard()
