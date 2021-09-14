from datetime import  date
from random import random

MAX_NUM = 100000000

pass_lst = []
tries = []


while len(pass_lst) < 10:
    number = str(int(random()* MAX_NUM))

    if len(number) != 8:
        continue

    year = int(number[4:8])
    month = int(number[2:4])
    day = int(number[:2])

    tries += tries

    try:
        date(year, month, day)

    except ValueError:
        if len(set(number)) == 8:
            pass_lst.append(number)

    for p in pass_lst:
        print(p)