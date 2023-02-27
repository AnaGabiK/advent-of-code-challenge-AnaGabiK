points_tipo = {
    'Rock': 1, 
    'Paper': 2, 
    'Scissors': 3
}
pontos_rodada = {
    'X': 0, 
    'Y': 3, 
    'Z': 6
}
draw = {
    'A': 'Rock', 
    'B': 'Paper', 
    'C': 'Scissors'
}
win = {
    'A' : 'Paper',
    'B' : 'Scissors',
    'C' : 'Rock'
}
lose = {
    'A' : 'Scissors',
    'B' : 'Rock',
    'C' : 'Paper'
}


with open('01-advent-of-code-challenge/02/sample.in', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

def jogo(round_string):
    elfo = round_string[0]
    decisao = pontos_rodada[round_string[2]]
    if decisao == 3:
      return pontos_rodada['Y'] + points_tipo[draw[elfo]]
    elif decisao == 0:
      return points_tipo[lose[elfo]]
    elif decisao == 6:
      return pontos_rodada['Z'] + points_tipo[win[elfo]]

print(sum([jogo(round_string) for round_string in rounds]))
