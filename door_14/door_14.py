from collections import defaultdict


def main():
    with open('push.txt') as p:
        push_ups = [int(line) for line in p.read().split(', ')]

    acc, acc_total = [push_ups[0]], defaultdict(list)
    for idx, (prev, curr) in enumerate(zip(push_ups, push_ups[1:])):
        if prev < curr:
            acc.append(curr)
        else:
            acc_total[idx].extend(acc)
            acc = [curr]

    for key, value in acc_total.items():
        is_lower = []
        for curr, nxt in zip(push_ups[key:], push_ups[key + 1:]):
            if curr > nxt:
                is_lower.append(nxt)
            else:
                acc_total[key].extend(is_lower)
                break

    aggregates = []
    for value in acc_total.values():
        print(value)
        aggregates.append((len(value), sum(value)))

    print(max(aggregates, key=lambda x: x[0])[1])


if __name__ == '__main__':
    main()
