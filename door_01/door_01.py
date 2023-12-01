import ast


def main():
    with open('bets.txt') as b, open('goals.txt') as g:
        bets = ast.literal_eval(b.readline())
        goals = ast.literal_eval(g.readline())

    init = 50_000
    wallet = init
    for [bet, odds], goals in zip(bets, goals):
        at_stake = round(wallet * 17.5 / 100)
        wallet += round(at_stake * odds) if bet <= goals else -at_stake

    print(init - wallet)


if __name__ == '__main__':
    main()
