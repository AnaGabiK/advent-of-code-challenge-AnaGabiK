import numpy as np

with open('01-advent-of-code-challenge/08/sample.in', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

arvores = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    arvores[i, :] = np.array(list(line))

arvores_visiveis = 2*len(lines[0]) + 2 *(len(lines)-2)

for i in range(1, arvores.shape[0]-1):
    for j in range(1, arvores.shape[1]-1):
        coluna = arvores[:, j] - arvores[i, j]
        linha = arvores[i, :] - arvores[i, j]
        routes = [linha[:j], linha[j+1:], coluna[:i], coluna[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            arvores_visiveis += 1

print(arvores_visiveis)