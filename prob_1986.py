n = int(input())
hexa = input().split()
palavra = ""

for i in range(n):
    palavra += chr(int(hexa[i], 16))

print(palavra)
