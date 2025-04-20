import time


def has_property(number_str):
    divs = [2, 3, 5, 7, 11, 13, 17]
    d = 0
    for i in range(7):
        substr = int(number_str[i + 1 : i + 4])
        if substr % divs[i] != 0:
            return False
    return True


def check_perms(n, a, print_interval=10000):
    c = [0 for i in range(n)]
    number = "".join(a)
    curr_perm = 1
    valids = [] if not has_property(number) else [int(number)]
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]
            number = "".join(a)
            if has_property(number):
                valids.append(int(number))
            if curr_perm % print_interval == 0:
                print(f"Checking: {curr_perm}", end="\r")
            curr_perm += 1
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1
    return valids


def main():
    input_list = list("0123456789")
    result = check_perms(len(input_list), input_list)
    print(result)
    print(sum(result))


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
