with open('01-advent-of-code-challenge/03/sample.in', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

def item_igual(line):
    line = list(line)

    meio = len(line) // 2
    primeiro_compart = line[:meio]
    segundo_compart = line[meio:]

    for i in primeiro_compart: 
        if i in segundo_compart:
            igual_char = i

    if igual_char.isupper():
        return(ord(igual_char) - 38)
    else:
        return(ord(igual_char) - 96)


print(sum([item_igual(j) for j in rounds]))