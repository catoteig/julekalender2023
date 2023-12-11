def main():
    with open('kart.txt') as k:
        kart = [[p for p in row] for row in k.read().splitlines()]

    islands, visited, land = 0, set(), 'X'
    x_dir, y_dir = len(kart), len(kart[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for x in range(x_dir):
        for y in range(y_dir):
            if kart[x][y] == land and (x, y) not in visited:
                traverse_pile = [(x, y)]
                while traverse_pile:  # bfs
                    current_x, current_y = traverse_pile.pop()
                    if 0 <= current_x < x_dir and 0 <= current_y < y_dir and kart[current_x][current_y] == land:
                        kart[current_x][current_y] = '.'
                        visited.add((current_x, current_y))
                        for dir_x, dir_y in directions:
                            traverse_pile.append((current_x + dir_x, current_y + dir_y))
                islands += 1

    print(islands)


if __name__ == '__main__':
    main()
