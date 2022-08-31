n_casos = int(input())

for casos in range(n_casos):
    x = int(input())
    y = True

    for i in range(2, x - 1):
        if x % i == 0:
            print(f"{x} nao eh primo")
            y = False
            break

    if y:
        print(f"{x} eh primo")
