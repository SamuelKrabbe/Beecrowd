positives = 0
soma = 0
for i in range(6):
    x = float(input())
    if x > 0:
        positives += 1
        soma += x
average = soma / positives
print(f"{positives} valores positivos\n{average:.1f}")
