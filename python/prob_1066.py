even = 0
positives = 0
negatives = 0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        even += 1
        odd = 5 - even
    if x > 0:
        positives += 1
    if x < 0:
        negatives += 1
print(
    f"{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{positives} valor(es) positivo(s)\n{negatives} valor(es) negativo(s)"
)
