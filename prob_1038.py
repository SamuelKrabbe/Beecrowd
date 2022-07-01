code, quant = input().split()
code = float(code)
quant = float(quant)
if code == 1:
    total = quant * 4.0
    print(f"Total: R$ {total:.2f}")
elif code == 2:
    total = quant * 4.5
    print(f"Total: R$ {total:.2f}")
elif code == 3:
    total = quant * 5.0
    print(f"Total: R$ {total:.2f}")
elif code == 4:
    total = quant * 2.0
    print(f"Total: R$ {total:.2f}")
else:
    total = quant * 1.5
    print(f"Total: R$ {total:.2f}")
