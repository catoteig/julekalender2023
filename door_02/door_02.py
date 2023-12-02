def main():
    with open('log.txt') as l:
        log = [[line.startswith('klikk'), int(line[-1:])] for line in l.readline().split(', ')]

    solved, progress = 0, [False] * 7
    for [click, cyl] in log:
        progress[cyl - 1] = True if click else False
        if all(i for i in progress):
            solved += 1
            progress = [False] * 7

    print(solved)


if __name__ == '__main__':
    main()
