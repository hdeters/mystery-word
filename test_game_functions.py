from mystery_word import *
from demon_words import *
from game_functions import *

word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]


def test_easy_words():
    assert easy_words(word_list) == \
        ["bird", "calf", "river", "stream", "brain"]


def test_medium_words():
    assert medium_words(word_list) == \
        ["stream", "kneecap", "cookbook", "language", "sneaker"]


def test_hard_words():
    assert hard_words(word_list) == \
        ["cookbook", "language", "algorithm", "integration"]


def test_random_word():
    """This test is not very good. Testing things that are random is hard, in
    that there's not a predictable choice. The best we can do is make sure
    we have valid output."""
    word = random_word(word_list)
    assert word in word_list


def test_display_word():
    word = "integration"
    assert display_word([], word) == "_ _ _ _ _ _ _ _ _ _ _"
    assert display_word(["z"], word) == "_ _ _ _ _ _ _ _ _ _ _"
    assert display_word(["g"], word) == "_ _ _ _ G _ _ _ _ _ _"
    assert display_word(["i"], word) == "I _ _ _ _ _ _ _ I _ _"
    assert display_word(["i","g"], word) == "I _ _ _ G _ _ _ I _ _"
    assert display_word(["i","n","z"], word) == "I N _ _ _ _ _ _ I _ N"


def test_still_playing():
    word = "river"
    assert still_playing(word, [])
    assert still_playing(word, ["r"])
    assert still_playing(word, ["r", "e"])
    assert still_playing(word, ["r", "e", "z"])
    assert not still_playing(word, ["r", "e", "v", "i"])

def test_choose_new_group():
    guess = "i"
    assert sorted(choose_new_group(word_list,guess)[1]) == sorted(["calf","cookbook","kneecap","language","sneaker","stream"])
    assert choose_new_group(word_list,guess)[0] == ("[]",6)
