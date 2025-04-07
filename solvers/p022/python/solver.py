import time
import csv

def main():
    with open('names.txt') as f:
        reader = csv.reader(f)
        names = next(reader)

    names.sort()
    total = 0
    i = 1
    for n in names:
        worth = 0
        for l in n:
            worth += ord(l) - 64
        score = i * worth
        total += score
        i += 1
    
    print(total)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
