import game_functions as gf
import random

#word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
#             "language", "sneaker", "algorithm", "integration", "brain"]

word_list = []
guess = ""

with open("/usr/share/dict/words") as filename:
    '''Read in dictionary of words'''
    for line in filename:
        word_list.append(line.strip().lower())

def get_length():
    '''Ask the user how long they want the word to be, check input, return length'''
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
    '''Ask the user how many guesses they want, check the input, return guesses'''
    guesses = input("How many guesses do you want?: ")
    try:
        the_guesses = int(guesses)
        if the_guesses > 0:
            return the_guesses
        else:
            print("Not a valid number")
            return get_guesses()
    except:
        print("Please enter a number")
        return get_guesses()

def find_initial_words(word_list,word_length):
    '''Get all words from the dictionary that are the specified length, return the list'''
    viable_words = []
    for word in word_list:
        if len(word) == word_length:
            viable_words.append(word)
    return viable_words

def is_guess_in_word(word_list,guess):
    '''Determine if the guess is in the word. Create groups for words without the guess
    and words with. Return both groups'''
    yes_group = []
    no_group = []
    for word in word_list:
        if guess in word:
            yes_group.append(word)
        else:
            no_group.append(word)
    return yes_group,no_group

def find_words_with_index(dict_with_words,idx):
    '''Given the dictionary of words and the index of the guess, as well as the most prevalent
    index, return a list of words with the guess at that index'''
    list_of_words = []
    #Returns a list of tuples with (word, indexes where guess is found)
    word_index_tuples = sorted(dict_with_words.items(), key=lambda x:(x[1]), reverse=True)
    for pair in word_index_tuples:
        if str(pair[1]) == str(idx):
            list_of_words.append(pair[0])
    return list_of_words

def choose_new_group(working_group,guess):
    '''Takes the current group of possible words and the guess. Creates a dictionary containing
    each word and the indexes at which the guess can be found. Creates a dictionary containing
    all of the indexes where the guess is found and how many words contain the guess at those indexes.
    Creates a sorted list of tuples from that dictionary so that we can find the most common indexes.
    Uses find_words_with_index to create a list of words that have the guess at the most common group of indexes.
    Returns the tuple containing the popular indexes and how popular they are as well as the list
    of words with the guess at those indexes.'''

    if len(working_group) == 0:
        return (0,0), []
    else:
        spots_dict = {}
        positionings = {}
        sorted_positionings = []

        for word in working_group:
            spots = [i for i, letter in enumerate(word) if letter == guess]
            spots_dict[word] = spots

        for key in spots_dict:
            idxs = str(spots_dict[key])
            if idxs in positionings:
                positionings[idxs] += 1
            else:
                positionings[idxs] = 1

        #returns a list of tuples with (idx of letters,how many times that idx appears) from most to least
        sorted_positionings = sorted(positionings.items(), key=lambda x:(x[1]), reverse=True)

        largest_occurence = sorted_positionings[0]

        list_of_words = find_words_with_index(spots_dict, largest_occurence[0])

        return largest_occurence,list_of_words

def ending(last_word,guessed_letters,guesses,guess):
    '''If there is only one possible word left, ending is called. It handles the rest of
    the game as if it is a normal game of hangman. Returns true if the player won, False if
    they lost'''
    while guesses > 0:
        if gf.still_playing(last_word,guessed_letters):
            guess = gf.ask_letter(guessed_letters)
            guessed_letters.append(guess)
            if guess in last_word:
                print("{} is in the word, guesses left:{}".format(guess,guesses))
                print(gf.display_word(guessed_letters, last_word))
                return ending(last_word,guessed_letters,guesses,guess)
            else:
                guesses -= 1
                print("{} is not in the word, guesses left:{}".format(guess,guesses))
                print(gf.display_word(guessed_letters, last_word))
                return ending(last_word,guessed_letters,guesses,guess)
        else:
            return True
    return False

def main_hard():
    '''Contains the primary while loop for the game.  Finds the initial options then enters the while loop.
    Checks if the player is on the last word, if so, calls ending(). Otherwise, asks for a guess,
    finds the lists that the guess is and isn't in. Then finds the most popular indexes and the words with
    the guess at those particular indexes. Determines if list of words with letter at most popular indexes
    or list of words that don't contain the guess is longer and chooses a word to display from that
    list.'''
    guessed_letters = []
    word_length = get_length()
    guesses = get_guesses()
    guess = ''

    initial_options = find_initial_words(word_list,word_length)

    while guesses > 0:
        if len(initial_options) == 1:
            win = ending(initial_options[0],guessed_letters,guesses,guess)
            if win:
                gf.play_again()
            else:
                print("You lose, the word was {}".format(initial_options[0]))
                gf.play_again()
        else:
            guess = gf.ask_letter(guessed_letters)
            guessed_letters.append(guess)

            list_letter_in, list_letter_not_in = is_guess_in_word(initial_options,guess)
            most_frequent_index,words_with_index = choose_new_group(list_letter_in,guess)

            if (most_frequent_index[1]) > len(list_letter_not_in):
                print_this = random.choice(words_with_index)
                initial_options = words_with_index
                print("\n{} is in the word, guesses left:{}".format(guess,guesses))
                print(gf.display_word(guessed_letters,print_this))
            else:
                print_this = random.choice(list_letter_not_in)
                initial_options = list_letter_not_in
                guesses -= 1
                print("\n{} is not in the word, guesses left:{}".format(guess,guesses))
                print(gf.display_word(guessed_letters,print_this))

    if guesses == 0:
        print("You lose, the word was {}".format(initial_options[0]))
        gf.play_again()

if __name__ == "__main__":
    main_hard()
