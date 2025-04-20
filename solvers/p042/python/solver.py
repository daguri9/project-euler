import time
import csv


def is_triangle(word):
    value = word_value(word)
    i = 0
    next_triangle = 1
    while next_triangle <= value:
        i += 1
        next_triangle = int((1 / 2) * i * (i + 1))
        if value == next_triangle:
            print(word)
            return True
    return False


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
        count += 1 if is_triangle(w) else 0

    print(count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
