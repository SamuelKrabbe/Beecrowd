litsa = map(int, input().split())
total = sum(litsa)
names = [
    "Dasher",
    "Dancer",
    "Prancer",
    "Vixen",
    "Comet",
    "Cupid",
    "Donner",
    "Blitzen",
    "Rudolph",
]
divi = total % 9

if divi == 0:
    winner = names[8]
else:
    for d in range(divi):

        winner = names[d]
