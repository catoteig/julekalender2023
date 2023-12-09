import ast
from collections import defaultdict


def main():
    with open('rekke.txt') as r:
        pairs = ast.literal_eval(r.read())

    neighbours = defaultdict(list)
    for (a, b) in pairs:
        neighbours[a].append(b)
        neighbours[b].append(a)

    curr = [n for n in neighbours if len(neighbours[n]) == 1].pop()

    used, elf_queue = {}, []
    while True:
        elf_queue.append(curr)
        used[curr] = True
        nxt_options = [n for n in neighbours[curr] if n not in used]
        if not nxt_options:
            break
        curr = nxt_options.pop()

    middle = len(elf_queue) // 2
    print(elf_queue[middle - 1] + elf_queue[middle])


if __name__ == '__main__':
    main()
