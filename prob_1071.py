num1 = int(input())
num2 = int(input())
soma = 0

# ordenando o intervalo de forma crescente
if num1 < num2:
    for i in range(num1 + 1, num2):
        if i % 2 != 0:
            soma += i
    print(soma)
elif num1 > num2:
    for i in range(num2 + 1, num1):
        if i % 2 != 0:
            soma += i
    print(soma)
else:
    print(num1 - num2)
