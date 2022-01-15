from nltk.corpus import words  # need nltk.download() corpus -> words at first use
import matplotlib.pyplot as plt
import pandas as pd

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
max = dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
print(max)

t = []

def is_contained_in_max(w):
    for c in w:
        if c not in max.keys():
            return False
    return True

for w in five_letters_words:
    if is_contained_in_max(w):
        t.append(w)

print(len(t))
print(t)
# plt.bar(data.keys(), data.values())
# plt.show()
