from random import randint


def highest_random(seed):
    highest = 0
    for i in range(5):
        r = randint(0, seed)
        if r > highest:
            highest = r
    msg = f"Highest random {highest:d}"
    return msg


print(highest_random(100))
