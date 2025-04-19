import time


def main():
    # The integer we want cannot have more than 4 digits
    candidates = [x for x in range(1, 9877) if len(set(str(x))) == len(str(x))]
    largest = 0
    for c in candidates:
        conc_prod = str(c)
        i = 2
        while len(conc_prod) < 9:
            prod = str(c * i)
            if (
                len(set(prod)) == len(prod)
                and set(prod) & set(conc_prod) == set()
                and "0" not in prod
            ):
                conc_prod += prod
                i += 1
            else:
                break
        if int(conc_prod) > largest:
            largest = int(conc_prod)

    print(f"{largest}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
