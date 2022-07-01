pedras, sapos = map(int, input().split())
posicoes_possiveis = []

for k in range(pedras):
    posicoes_possiveis.append(0)

for i in range(sapos):
    posicao_sapo, pulo = map(int, input().split())
    index_sapo = posicao_sapo - 1
    posicoes_possiveis[index_sapo] = 1

    while True:
        index_sapo += pulo
        if index_sapo < len(posicoes_possiveis):
            posicoes_possiveis[index_sapo] = 1
        else:
            break

    while True:
        index_sapo -= pulo
        if index_sapo >= 0:
            posicoes_possiveis[index_sapo] = 1
        else:
            break

for m in posicoes_possiveis:
    print(m)
