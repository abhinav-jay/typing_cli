from data.words import words
from engine.wordselect import makelist
import engine.test as test
import engine.typing as typing
import engine.results as results

nb_words = int(input("enter number of words:"))


def main():
    word_list = makelist(words, nb_words)

    # test.test(word_list)
    usr_input, time = typing.init(word_list)
    if time == 0 and usr_input == 0:
        main()

    accuracy, wpm = test.test(usr_input, word_list, time)
    results.init(accuracy, wpm)


while 1:
    main()
