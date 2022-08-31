lista = [0]
rep = 1

for i in range(1, 101):
    n = int(input())
    lista.append(n)

    if lista[0] > lista[1]:
        lista.remove(lista[1])
        maior = lista[0]
        n_input = i - rep
        rep += 1
    else:
        lista.remove(lista[0])
        maior = lista[0]
        n_input = i
        rep = 1

print(maior)
print(n_input)
