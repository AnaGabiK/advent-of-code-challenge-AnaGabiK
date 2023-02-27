tipo_input = {'A': 'Rock', 
             'B': 'Paper', 
             'C': 'Scissors', 
             'X': 'Rock', 
             'Y': 'Paper', 
             'Z': 'Scissors'}

pontos_tipo = {'Rock': 1, 
                    'Paper': 2, 
                    'Scissors': 3}

pontos_resultado = {'Lose': 0, 
                      'Draw': 3, 
                      'Win': 6}

with open('01-advent-of-code-challenge/02/sample.in', 'r') as f:
    linha = f.readlines()
    rodada = [entry.strip() for entry in linha]

def jogo(round_string):
    opponent_shape = tipo_input[round_string[0]]
    our_shape = tipo_input[round_string[2]]
    if opponent_shape == our_shape:
        return pontos_resultado['Draw'] + pontos_tipo[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return pontos_resultado['Lose'] + pontos_tipo[our_shape]
    else:
        return pontos_resultado['Win'] + pontos_tipo[our_shape]

print(sum([jogo(round_string) for round_string in rodada]))
