quant_exp = int(input())
total_cobaia = 0
total_coelho = 0
total_rato = 0
total_sapo = 0


for i in range(quant_exp):
    quant_cobaia, tipo_cobaia = input().split()
    quant_cobaia = int(quant_cobaia)
    total_cobaia += quant_cobaia
    if tipo_cobaia == "C":
        total_coelho += quant_cobaia
    elif tipo_cobaia == "R":
        total_rato += quant_cobaia
    else:
        total_sapo += quant_cobaia

per_coelho = (total_coelho / total_cobaia) * 100
per_rato = (total_rato / total_cobaia) * 100
per_sapo = (total_sapo / total_cobaia) * 100

print(f"Total: {total_cobaia} cobaias")
print(f"Total de coelhos: {total_coelho}")
print(f"Total de ratos: {total_rato}")
print(f"Total de sapos: {total_sapo}")
print(f"Percentual de coelhos: {per_coelho:.2f} %")
print(f"Percentual de ratos: {per_rato:.2f} %")
print(f"Percentual de sapos: {per_sapo:.2f} %")
