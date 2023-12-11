def main():
    with open('sjokkis.txt') as s:
        file = [[_ == '1' for _ in line] for line in s.read().splitlines()]
        sjokkis = [[plate[_:_ + 8] for _ in range(8)] for plate in file]

        print('💩' * 100)  # Saving for... later


if __name__ == '__main__':
    main()
