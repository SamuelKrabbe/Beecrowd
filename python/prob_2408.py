n = input().split()
podium = []

for i in n:
    podium.append(int(i))

podium.sort()

print(podium[1])
