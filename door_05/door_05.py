def main():
    goal = 100_000_000
    primes = sieve_of_eratosthenes(goal)

    total = 0
    for _ in range(1, goal):
        divided = _ / sum_digits(_)
        if divided % 1 == 0:
            if divided in primes:
                total += 1

    print(total)


# From the Internet:
def sieve_of_eratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    primes = {}
    for p in range(2, num + 1):
        if prime[p]:
            primes[p] = True
    return primes


# Also from the Internet
def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


if __name__ == '__main__':
    main()
