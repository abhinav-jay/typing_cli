import time

def test(words, usr_input, time):

    characters = break_chr(words)
    input_chr = break_chr(usr_input)
    wpm = wpm_calc(words, time)
    print(wpm, "wpm speed")
    print(accuracy(input_chr, characters))


def wpm_calc(words, time):
    time_min = time/60
    return int(round(len(words)/(5 * time_min)))


def break_chr(words):
    characters = []
    for character in words:
        characters.append(character)

    return characters


def accuracy(lst_test, lst_ref):
    correct_chr = 0

    for i in range(len(lst_ref)):
        if lst_ref[i] == lst_test[i]:
            correct_chr += 1

    return(str(int(round((correct_chr/len(lst_ref))*100))) + "% accuracy")
