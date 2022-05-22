caso_de_teste = int(input())

for c in range(caso_de_teste):
    anos = 0
    pa, pb, ga, gb = map(float, input().split())

    while pa <= pb:
        pa += pa * ga // 100

        pb += pb * gb // 100

        anos += 1

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
