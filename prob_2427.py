lado = int(input())
pedacos = 1

while lado >= 2:
    pedacos *= 4
    lado /= 2

print(pedacos)
