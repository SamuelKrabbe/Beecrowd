sal = float(input())

if sal >= 0 and sal <= 2000:
    imposto = "Isento"

    print(imposto)

elif sal >= 2000.01 and sal <= 3000:
    imposto = (sal - 2000) * 0.08

    print(f"R$ {imposto:.2f}")

elif sal >= 3000.01 and sal <= 4500:
    imposto = (1000 * 0.08) + ((sal - 3000) * 0.18)

    print(f"R$ {imposto:.2f}")

elif sal > 4500:
    imposto = (1000 * 0.08) + (1500 * 0.18) + ((sal - 4500) * 0.28)

    print(f"R$ {imposto:.2f}")
