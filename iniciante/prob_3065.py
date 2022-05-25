while True:
    n = int(input())
    x = 1

    if n == 0:
        break

    tudo = input()
    total = 0
    litsa = []

    for j in tudo:
        if j != "+" and j != "-":
            litsa.append(int(j))

    total = sum(litsa)

    for i in range(1, len(tudo), 2):
        if tudo[i] == "-":
            total -= int(tudo[i + 1])

    print("Teste {}".format(x))
    print(total)
    x += 1
