def main():
    with open('input.txt') as f:
        prices = [[int(price) for price in line.split(',')] for line in f.read().splitlines()]

    wallet, num_stocks = 200_000, 0
    for day in prices:
        max_diff, low, high = 0, 0, 0

        for (idx, left) in enumerate(day):
            for right in day[idx:]:
                diff = right - left
                if diff > max_diff:
                    max_diff, low, high = diff, left, right

        num_stocks = wallet // low
        wallet -= num_stocks * low
        wallet += num_stocks * high

    print(wallet)


if __name__ == '__main__':
    main()
