with open('01-advent-of-code-challenge/06/sample.in', 'r') as f:
    line = f.readline().strip()

for i in range(len(line)):
    packet = set(line[i:i+4])
    if len(packet) == 4:
        print(i+4)
        break