n = int(input())
candidatos = input().split()
vieram = 0

for i in range(n):
    if candidatos[i] == "1":
        vieram += 1

print(vieram)
