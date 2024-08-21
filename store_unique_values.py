import random

all_words = "all the words in the all world".split()


def get_random_word():
    return random.choice(all_words)


def get_unique_words():
    words = set()
    for _ in range(1000):
        words.add(get_random_word())
    return words


print(get_unique_words())
