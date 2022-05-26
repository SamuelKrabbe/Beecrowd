x = 1
while True:
    n = int(input())

    if n == 0:
        break

    tudo = input()
    lista = tudo.replace("+", " ").replace("-", " ").split()

    operadores = [op for op in tudo if op == "+" or op == "-"]

    total = int(lista[0])

    for i in range(len(operadores)):
        if operadores[i] == "+":
            total += int(lista[i + 1])
        else:
            total -= int(lista[i + 1])

    print("Teste {}".format(x))
    print(total)
    print()

    x += 1
