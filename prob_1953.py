while True:
    try:
        n = int(input())
        EPR = 0
        EHD = 0
        INTRUSOS = 0

        for i in range(n):
            inutil, curso = input().split()

            if curso == "EPR":
                EPR += 1
            elif curso == "EHD":
                EHD += 1
            else:
                INTRUSOS += 1

        print("EPR:", EPR)
        print("EHD:", EHD)
        print("INTRUSOS:", INTRUSOS)

    except:
        break
