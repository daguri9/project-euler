import time


def main():
    digits = set("123456789")
    pairs = []
    products = []
    for i in range(123, 9877):
        i_str = str(i)
        if "0" in i_str:
            continue
        i_charset = set(i_str)

        if len(i_str) == len(i_charset):
            for j in range(1, 100):
                j_str = str(j)
                if "0" in j_str:
                    continue
                j_charset = set(j_str)
                if (
                    len(j_str) == len(j_charset)
                    and (i_charset & j_charset) == set()
                ):
                    remaining = digits - i_charset - j_charset
                    prod = i * j
                    is_pandig = True
                    for c in str(prod):
                        if c not in remaining:
                            is_pandig = False
                            break
                        remaining.remove(c)
                    if is_pandig and len(remaining) == 0 and prod not in products:
                        pairs.append((i, j))
                        products.append(prod)

    print(f"Multiplicand, multiplier pairs: {pairs}")
    print(f"{sum(products)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
