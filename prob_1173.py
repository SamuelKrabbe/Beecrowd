n_casos = int(input())
lista_v = []

for ç in range(10):
    lista_v.append(n_casos)
    n_casos *= 2
    print(f"N[{ç}] = {lista_v[ç]}")
