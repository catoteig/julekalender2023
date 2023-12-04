def main():
    with open('reps.txt') as f:
        reps = [int(rep) for rep in f.read().split(', ')]

    acc, acc_total = [reps[0]], []
    for prev, curr in zip(reps, reps[1:]):
        if prev < curr:
            acc.append(curr)
        else:
            acc_total.append((len(acc), sum(acc)))
            acc = [curr]

    # To account for several of same length:
    max_count_items = [s[1] for s in acc_total if s[0] == max(acc_total, key=lambda v: v[0])[0]]
    print(max(max_count_items))


if __name__ == '__main__':
    main()
