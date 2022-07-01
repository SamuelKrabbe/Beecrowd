a, b = map(int, input().split())
if a == b:
    c = a
    print(c)
elif a != b and a > b:
    c = a
    print(c)
elif a != b and a < b:
    c = b
    print(c)
