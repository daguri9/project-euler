from num2words import num2words
import time

def main():
    word_count = 0
    for i in range(1, 1001):
        word_count += len(num2words(i).translate({ord(k):None for k in u' -'}))
    
    print(word_count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")