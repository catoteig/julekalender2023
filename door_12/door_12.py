import string


def sieve_of_eratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)
    return primes


def twin_primes(n):
    all_primes = sieve_of_eratosthenes(n)
    found_twin_primes = []
    for prev, curr in zip(all_primes, all_primes[1:]):
        if curr == 2 or prev == 2:
            continue
        if curr - prev == 2:
            found_twin_primes.append((prev, curr))
    return found_twin_primes


def decrypt(letter, key):
    letters_lower, letters_upper = string.ascii_lowercase, string.ascii_uppercase
    if letter.islower():
        return letters_lower[(letters_lower.find(letter) - key) % len(letters_lower)]
    elif letter.isupper():
        return letters_upper[(letters_upper.find(letter) - key) % len(letters_upper)]
    else:
        return letter


def binaries_even_1s(up_to):
    binaries, i = [], 0
    while len(binaries) < up_to:
        if bin(i).count('1') % 2 == 0:
            binaries.append(i)
        i += 1
    return binaries


def main():
    encrypted, decrypted = 'Ojfkyezkz bvclae zisj a guomiwly qr tmuematbcqxqv sa zmcgloz.', ''

    x = len(twin_primes(6**6 + 666))
    y = binaries_even_1s(len(encrypted))

    for idx, letter in enumerate(encrypted):
        key = x * y[idx]
        decrypted += decrypt(letter, key)

    print(decrypted)


if __name__ == '__main__':
    main()
