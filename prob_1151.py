count = int(input())

x = 0
y = 1
for c in range(count - 1):
    fib = x + y

    print(x, end=" ")

    x = y
    y = fib

print(x)
