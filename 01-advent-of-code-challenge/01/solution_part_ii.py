import fileinput

soma = 0
total = 0
calorias = []

for line in fileinput.FileInput("01-advent-of-code-challenge/01/sample.in"):
  if line.strip() == "":
    calorias.append(soma)
    soma = 0
  else:
    valor = [int(i) for i in line.split() if i.isdigit()]
    valor = valor[0]
    soma = valor + soma

for i in range (3):
  maior = max(calorias)
  calorias.remove(maior)
  total += maior 
  
print(total)