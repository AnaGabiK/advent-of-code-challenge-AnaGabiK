with open("01-advent-of-code-challenge/01/sample.in", "r") as f:
    linhas = f.readlines()
    calorias = [entrada.strip() for entrada in linhas]


soma_elfos = []
soma_atual = 0
for entrada in calorias:
    if entrada != "":
        soma_atual += int(entrada)
    elif entrada == "":
        soma_elfos.append(soma_atual)
        soma_atual = 0
soma_elfos.append(soma_atual)

print(max(soma_elfos))