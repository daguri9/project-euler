import time
import csv
from math import sqrt

def is_triangle(t):
    n = (1/2)*(sqrt(8*t + 1)-1)
    return n.is_integer()


def word_value(word):
    value = 0
    for l in word:
        value += ord(l) - 64
    return value


def main():
    with open("words.txt") as f:
        reader = csv.reader(f)
        words = next(reader)


    count = 0
    for w in words:
        val = word_value(w)
        count += 1 if is_triangle(val) else 0

    print(count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.6f} seconds.")
