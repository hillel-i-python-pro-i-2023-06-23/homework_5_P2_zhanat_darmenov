import random


def starting_point():
    while True:
        flipper = random.randint(0, 100)
        print(f"Randomized Value: {100 * flipper}")


if __name__ == "__main__":
    starting_point()
