from nltk.corpus import words  # need nltk.download() corpus -> words at first use
import matplotlib.pyplot as plt
import pandas as pd
import random

word_list = words.words()
# prints 236736
print(len(word_list))


def check_len_five(word):
    return len(word) == 5


def get_five_letters_words_only(wl=word_list):
    five_letters_words_iterator = filter(check_len_five, wl)
    five_letters_words = list(five_letters_words_iterator)
    return [s.lower() for s in five_letters_words]


five_letters_words = get_five_letters_words_only()

print(f"{len(five_letters_words)} five letter words")


def letter_count(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0)+1
    return d


def get_word_list_letter_count(words):
    lc_sum = {}
    for w in words:
        lc = letter_count(w)
        lc_sum = {k: lc.get(k, 0) + lc_sum.get(k, 0)
                  for k in set(lc) | set(lc_sum)}
    return lc_sum


data = dict(sorted(get_word_list_letter_count(five_letters_words).items()))

import operator
top_ten = dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
print(f"Top 10 letters with occurences: : {top_ten}")


def is_contained_in_top(w, top=top_ten):
    for c in w:
        if c not in top.keys():
            return False
    return True

words_in_top_ten = []

for w in five_letters_words:
    if is_contained_in_top(w):
        words_in_top_ten.append(w)


# print(f"len(words_in_top_ten) words are composed of top ten letters only:" )
# print(words_in_top_ten)


def get_strat(top=15):
    top_15 = dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:top])
    strat_words = []
    for i in range(2*len(five_letters_words)):
        w = random.choice(five_letters_words)
        if is_contained_in_top(w, top=top_15):
            strat_words.append(w)
            top_15_copy = dict(top_15)
            for c in w:
                top_15_copy.pop(c, None)
            top_15 = top_15_copy
    missing_letters = []
    if len(top_15.keys()) > 0:
        missing_letters = list(top_15.keys())
    return strat_words, f"missing letters : {missing_letters}"
    

print(f"get a strat for 10: {get_strat(10)}")
print(f"get a strat for 15: {get_strat()}")

def greedy_strat():
    print("Looking for a greedy strat")
    strat, ml = get_strat(10)
    while len(ml) > 22:
        strat, ml = get_strat(10)
    print(f"get a strat for 10: {strat, ml}")
    strat, ml = get_strat(15)
    while len(ml) > 22:
        strat, ml = get_strat(15)
    print(f"get a strat for 15: {strat, ml}")

greedy = True
if(greedy):
    greedy_strat()
# if you wanna see cool plot
# plt.bar(data.keys(), data.values())
# plt.show()
