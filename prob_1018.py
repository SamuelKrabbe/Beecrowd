value = int(input())
notes_100 = value // 100
notes_50 = (value % 100) // 50
notes_20 = ((value % 100) % 50) // 20
notes_10 = (((value % 100) % 50) % 20) // 10
notes_5 = ((((value % 100) % 50) % 20) % 10) // 5
notes_2 = (((((value % 100) % 50) % 20) % 10) % 5) // 2
notes_1 = ((((((value % 100) % 50) % 20) % 10) % 5) % 2) // 1

print(value)
print(notes_100, "nota(s) de R$ 100,00")
print(notes_50, "nota(s) de R$ 50,00")
print(notes_20, "nota(s) de R$ 20,00")
print(notes_10, "nota(s) de R$ 10,00")
print(notes_5, "nota(s) de R$ 5,00")
print(notes_2, "nota(s) de R$ 2,00")
print(notes_1, "nota(s) de R$ 1,00")
