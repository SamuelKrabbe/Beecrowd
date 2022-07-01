t_cases = int(input())
x = 0
y = 1
lista = [x, y]

for cases in range(t_cases):
    n = int(input())

    for numbers in range(n):
        fib = x + y
        lista.append(fib)
        x = y
        y = fib

    print(f"Fib({n}) = {lista[n]}")
