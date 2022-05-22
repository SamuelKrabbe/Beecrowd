while True:
    n = int(input())

    if n == 0:
        break

    if n % 2 == 0:
        soma = n

        for numbers in range(4):
            n += 2
            soma += n

        print(soma)
    else:
        n = n + 1
        soma = n

        for numbers in range(4):
            n += 2
            soma += n

        print(soma)
