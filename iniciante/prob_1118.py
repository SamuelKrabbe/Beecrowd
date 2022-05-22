x = True

while x == True:
    y = 0
    soma = 0

    while y < 2:
        num = float(input())

        if 0 <= num <= 10:
            soma += num
            y += 1
        else:
            print("nota invalida")

        media = soma / 2

    print(f"media = {media:.2f}")

    dnovo = int(input("novo calculo (1-sim 2-nao)\n"))

    while dnovo < 1 or dnovo > 2:
        dnovo = int(input("novo calculo (1-sim 2-nao)\n"))

    if dnovo == 2:
        x = False
