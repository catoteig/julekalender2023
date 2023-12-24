import string


def main():
    transaksjoner = [[el[0], int(el[1]), int(el[2])] for el in (line.split(';') for line in open('transaksjoner.txt'))]
    alphabet = {letter: index for index, letter in enumerate(list(string.ascii_lowercase) + ['æ', 'ø', 'å'], 1)}
    hx = int('0xbeef', 16)

    valid = ''
    for tittel, pris, hash in transaksjoner:
        tittel_sum = sum(alphabet[l] for l in tittel.lower() if l in alphabet.keys())
        valid += tittel[0] if (tittel_sum * pris) % hx != hash else ''

    print(valid)


if __name__ == '__main__':
    main()
