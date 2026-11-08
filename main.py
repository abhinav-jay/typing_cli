from data.words import words
from engine.wordselect import makelist
import engine.test as test
import engine.typing as typing

nb_words = int(input("enter number of words:"))

word_list = makelist(words, nb_words)

# test.test(word_list)

usr_input, time = typing.init(word_list)
test.test(usr_input, word_list, time)
