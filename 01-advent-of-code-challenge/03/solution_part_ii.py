with open('01-advent-of-code-challenge/03/sample.in', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

soma = 0
while len(rounds) > 0:
    primeiro = set(rounds.pop())
    segundo = set(rounds.pop())
    terceiro = set(rounds.pop())

    letra_igual = ((primeiro.intersection(segundo)).intersection(terceiro)).pop()

    if letra_igual.isupper():
        soma += ord(letra_igual) - 38
    else:
        soma += ord(letra_igual) - 96

print(soma)