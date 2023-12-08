import ast
import string


def main():
    with open('cypher.txt') as c, open('input.txt') as i:
        input_list = [ast.literal_eval(line) for line in i.read().splitlines()]
        cypher = [line.split(' ') for line in c.read().splitlines() if line.strip()]
        cypher_flatmap = [el for sub_list in cypher for el in sub_list]

    alphabet = list(string.ascii_lowercase) + ['æ', 'ø', 'å']

    decrypted_cypher = []
    for cyp, key in zip(cypher_flatmap, input_list):
        key_dict = {alphabet[key[idx]]: letter for idx, letter in enumerate(alphabet)}
        key_dict[','] = ','
        decrypted_cypher.append(''.join(key_dict[letter] for letter in cyp))

    solution = ''
    for line_length in [len(i) for i in cypher]:
        solution += decrypted_cypher[:line_length][0][0]
        del decrypted_cypher[:line_length]

    print(solution)


if __name__ == '__main__':
    main()
