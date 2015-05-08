from mystery_word_hard import *

word_list = ["bird", "calf", "river", "iriri", "stream","begin","iowan","imide","igrii", "kneecap",  "cookbook",
              "language", "sneaker", "algorithm", "integration", "brain"]

word=("bird", [1])
word_length = 5
guess = "i"
yes_group = ['river', 'iriri', 'begin', 'iowan', 'imide', 'igrii', 'brain']
big_group = [('brain', [3]), ('iowan', [0]), ('river', [1]), ('begin', [3])]

def test_find_viable_words():
    assert find_viable_words(word_list,word_length) == \
        ["river", "iriri", "begin", "iowan", "imide", "igrii", "brain"]

def test_choose_new_group():
    assert sorted(choose_new_group(yes_group)) == \
        sorted([('brain', [3]), ('iowan', [0]), ('river', [1]), ('begin', [3])])

def test_choose_best_position():
    assert choose_best_position(big_group) == \
        [('brain', [3]), ('begin', [3])]
