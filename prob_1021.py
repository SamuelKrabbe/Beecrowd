money = float(input())
note100 = money // 100
note50 = (money % 100) // 50
note20 = ((money % 100) % 50) // 20
note10 = (((money % 100) % 50) % 20) // 10
note5 = ((((money % 100) % 50) % 20) % 10) // 5
note2 = (((((money % 100) % 50) % 20) % 10) % 5) // 2
money_conversion = ((((((money % 100) % 50) % 20) % 10) % 5) % 2) * 100
i = int(money_conversion)
coin1 = i // 100
coin05 = (i % 100) // 50
coin025 = ((i % 100) % 50) // 25
coin010 = (((i % 100) % 50) % 25) // 10
coin005 = ((((i % 100) % 50) % 25) % 10) // 5
coin001 = ((((i % 100) % 50) % 25) % 10) % 5

print("NOTAS:")
print(f"{int(note100)} nota(s) de R$ 100.00")
print(f"{int(note50)} nota(s) de R$ 50.00")
print(f"{int(note20)} nota(s) de R$ 20.00")
print(f"{int(note10)} nota(s) de R$ 10.00")
print(f"{int(note5)} nota(s) de R$ 5.00")
print(f"{int(note2)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(coin1)} moeda(s) de R$ 1.00")
print(f"{int(coin05)} moeda(s) de R$ 0.50")
print(f"{int(coin025)} moeda(s) de R$ 0.25")
print(f"{int(coin010)} moeda(s) de R$ 0.10")
print(f"{int(coin005)} moeda(s) de R$ 0.05")
print(f"{int(coin001)} moeda(s) de R$ 0.01")
