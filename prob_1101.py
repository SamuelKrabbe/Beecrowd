while True:
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break
    elif x < y:
        soma = x
        n = x
        lista = [x]
        for i in range(abs(y - x)):
            n += 1
            soma += n
            lista.append(n)
    else:
        soma = y
        n = y
        lista = [y]
        for i in range(abs(y - x)):
            n += 1
            soma += n
            lista.append(n)

    print(*lista, f"Sum={soma}")
