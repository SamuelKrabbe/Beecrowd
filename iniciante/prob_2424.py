n = input().split()
ball_coods = []

for i in n:
    ball_coods.append(int(i))

if (0 <= ball_coods[0] <= 432) and (0 <= ball_coods[1] <= 468):
    print("dentro")
else:
    print("fora")
