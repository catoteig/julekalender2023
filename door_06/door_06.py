import math


def main():
    with open('rute.txt') as f:
        route = [tuple(int(c) for c in city.split(',')) for city in f.read().splitlines()]

    reindeers, traveled = 9, 0
    for (x0, y0), (x1, y1) in zip(route, route[1:]):
        traveled += math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2)

    food_consumed = math.ceil((traveled * reindeers) / 1000)

    print(food_consumed)


if __name__ == '__main__':
    main()
