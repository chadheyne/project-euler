#!/usr/bin/env python
from datetime import date

MONTHS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
YEARS = range(1901, 2001)


def main():
    first_sunday = 0
    for year in YEARS:
        for month in MONTHS:
            day = date(year, month, 1)
            if day.isoweekday() == 7:
                first_sunday += 1
    print(first_sunday)


if __name__ == "__main__":
    main()
