lista1 = input().split()
lista2 = input().split()
code1, num_unit1, price_unit1 = lista1
code2, num_unit2, price_unit2 = lista2
total = (int(num_unit1) * float(price_unit1)) + (int(num_unit2) * float(price_unit2))

print(f"VALOR A PAGAR: R$ {total:.2f}")
