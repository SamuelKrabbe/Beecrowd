x = int(input())
y = int(input())

if x < y:
    for c in range(x, y - 1):
        x += 1
        if (x % 5 == 2) or (x % 5 == 3):
            print(x)
else:
    for c in range(y, x - 1):
        y += 1
        if (y % 5 == 2) or (y % 5 == 3):
            print(y)
