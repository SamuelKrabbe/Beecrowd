carros, voltas = map(int, input().split())
tempos = []

if voltas == 1:
    split = False
else:
    split = True

for i in range(carros):
    if split:
        n = input().split()
        total_carro = 0

        for tempo in n:
            total_carro += int(tempo)

        tempos.append(total_carro)
    else:
        n = int(input())
        tempos.append(n)

tempos_ordenados = list(tempos)
tempos_ordenados.sort()
melhores = []

for j in range(3):
    k = tempos.index(tempos_ordenados[j]) + 1
    melhores.append(k)

for melhor in melhores:
    print(melhor)
