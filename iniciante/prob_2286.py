x = 1

while True:
    n = int(input())

    if n == 0:
        break

    ganhador = []

    nome1 = input()
    nome2 = input()

    for i in range(n):
        j1, j2 = map(int, input().split())

        if (j1 + j2) % 2 == 0:
            ganhador.append(nome1)
        else:
            ganhador.append(nome2)

    print("Teste {}".format(x))
    x += 1

    for j in range(len(ganhador)):
        print(ganhador[j])
