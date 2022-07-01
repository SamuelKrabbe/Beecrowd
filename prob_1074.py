n = int(input())


def even_or_odd(x):

    if x > 0:
        if x % 2 == 0:
            print(f"EVEN POSITIVE")
        else:
            print(f"ODD POSITIVE")
    elif x < 0:
        if x % 2 == 0:
            print(f"EVEN NEGATIVE")
        else:
            print(f"ODD NEGATIVE")
    else:
        print("NULL")


for i in range(n):
    number = int(input())
    even_or_odd(number)
