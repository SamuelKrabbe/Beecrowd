porcao_curupira = 300
porcao_boitata = 1500
porcao_boto = 600
porcao_mapinguari = 1000
porcao_iara = 150

curupira = int(input())
boitata = int(input())
boto = int(input())
mapinguari = int(input())
iara = int(input())

total = (
    225
    + (porcao_curupira * curupira)
    + (porcao_boitata * boitata)
    + (porcao_boto * boto)
    + (porcao_mapinguari * mapinguari)
    + (porcao_iara * iara)
)
print(total)
