import time


def main():
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first_day_yr = 1
    sunday_count = 0
    for year in range(1901, 2001, 1):
        first_day_yr = (
            (1 + first_day_yr) % 7 if year % 4 != 1 else (2 + first_day_yr) % 7
        )
        days_per_month[1] = 29 if year % 4 == 0 else 28
        for m in range(12):
            first = days_per_month[m - 1] + first if m > 0 else 1
            day = (first + first_day_yr - 1) % 7
            sunday_count += 1 if day == 0 else 0

    print(sunday_count)


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
