def main():
    concat, items = '', 0
    for _ in range(0, 100_000):
        s = str(_)
        if s not in concat:
            items += 1
            concat += s

    print(items)


if __name__ == '__main__':
    main()
