from num2words import num2words

def compute():
    word_count = 0
    for i in range(1, 1001):
        word_count += len(num2words(i).translate({ord(k):None for k in u' -'}))
    return word_count


if __name__ == "__main__":
    print(compute())