values = input().split()
a, b, c = values
a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    print(a, "eh o maior")
else:
    if b >= a and b >= c:
        print(b, "eh o maior")
    else:
        print(c, "eh o maior")
