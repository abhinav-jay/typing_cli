import random

def makelist(words, nb_words):
    ans = ""
    for i in range(nb_words):
        ans += random.choice(words)
        ans += " "

    ans = ans.strip()
    return ans

