x = 0
j = 0

while x <= 2.0:
    for i in range(3):
        x = round(x, 1)
        j += 1
        if x % 1 == 0:
            print(f"I={int(x)} J={int(j)}")
        else:
            print(f"I={x:.1f} J={j:.1f}")
    x += 0.2
    j = 0 + x
