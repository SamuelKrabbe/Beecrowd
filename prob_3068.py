t = 1
while True:
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break

    qnt_met = int(input())

    dentro_da_fzd = 0

    for i in range(qnt_met):
        x_met, y_met = map(int, input().split())

        if (x1 <= x_met and x_met <= x2) and (y1 >= y_met and y_met >= y2):
            dentro_da_fzd += 1

    print("Teste {}".format(t))
    print(dentro_da_fzd)
    t += 1
