lista_vetor = []

for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
        lista_vetor.append(x)
    else:
        lista_vetor.append(x)
    print(f"X[{i}] = {lista_vetor[i]}")
