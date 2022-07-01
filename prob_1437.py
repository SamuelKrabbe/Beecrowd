dir = ["N", "L", "S", "O"]

while True:
    n = int(input())
    x = 0

    if n == 0:
        break

    comandos = input()

    for cmd in comandos:
        if x == 4 or x == -4:
            x = 0

        if cmd == "D":
            x += 1
        else:
            x -= 1

    virou = dir[x]
    print(virou)
