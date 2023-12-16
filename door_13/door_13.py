def sieve_of_eratosthenes(num):
    prime = [True for i in range(num)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, num):
        if prime[p]:
            primes.append(p)
    return primes


def main():
    with open('grinchen.txt') as g, open('alver_på_jobb.txt') as at, open('alver_ikke_på_jobb.txt') as not_at:
        grinchen = [int(line) for line in g.read().splitlines()]
        at_work = [int(line) for line in at.read().splitlines()]
        not_at_work = [int(line) for line in not_at.read().splitlines()]

    windows = 400_009
    window_list = [False] * windows
    primes = sieve_of_eratosthenes(1_000_000_000)
    window_1 = lambda i: (i * 2) % windows
    window_2 = lambda i: (i + primes[i]) % windows

    for elf in at_work:
        window_list[window_1(elf)], window_list[window_2(elf)] = True, True

    got_grinched = 0
    for elf in not_at_work:
        w1, w2 = window_1(elf), window_2(elf)
        if window_list[w1] and window_list[w2]:
            if w1 in grinchen or w2 in grinchen:
                got_grinched += 1

    print(got_grinched)


if __name__ == '__main__':
    main()
