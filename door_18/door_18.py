import os
import numpy as np


def main():
    total = 0
    for filename in os.listdir('graphs'):
        f = os.path.join('graphs', filename)

        with open(f) as g:
            graph = g.read().splitlines()
            transactions = [int(line) for line in graph.pop().split(', ')]
            transactions.reverse()

        np_arr = np.array([list(p) for p in graph])
        np_arr = np_arr.transpose()
        arr = np_arr.tolist()

        height = len(arr[0])
        transaction_days = []
        for day in arr:
            if 'K' in day:
                transaction_days.append([-transactions.pop(), height - day.index('K')])
            if 'S' in day:
                transaction_days.append([transactions.pop(), height - day.index('S')])

        for volume, price in transaction_days:
            total += volume * price

    print(total)


if __name__ == '__main__':
    main()
