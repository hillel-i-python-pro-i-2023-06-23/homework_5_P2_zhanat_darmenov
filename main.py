import random


def starting_point():
    looper = 0

    while looper < 10:
        flipper = random.randint(0, 100)
        print(f"Randomized Value: {100 * flipper}")
        looper += 1


if __name__ == "__main__":
    starting_point()
