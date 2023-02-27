with open('01-advent-of-code-challenge/04/sample.in', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

soma = 0

for line in rounds:
    parte_um, parte_dois = line.split(',')

    comeco_um, fim_um = map(int, parte_um.split('-'))
    comeco_dois, fim_dois = map(int,parte_dois.split('-'))

    if comeco_um <= comeco_dois and fim_um >= fim_dois:
        soma += 1
    elif comeco_um >= comeco_dois and fim_um <= fim_dois:
        soma += 1

print(soma)