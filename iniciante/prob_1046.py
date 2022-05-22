# lendo a hora inicial e a hora final de um jogo
hr_i, hr_f = map(int, input().split())

"""
Calculando a duração do jogo, sendo que o jogo tem duração 
minima de 1h e máxima de 24h, além disso, ele pode começar 
em um dia e terminar no outro
"""
if hr_i > hr_f:
    """
    Esse primeiro caso é para a situação em que o jogo vai de um dia ao outro
    """
    duracao = abs((hr_i - hr_f) - 24)
    print(f"O JOGO DUROU {duracao} HORA(S)")
elif hr_i < hr_f:
    """
    Nesse caso, é a situação em que o jogo acabou no mesmo
    dia que começou
    """
    duracao = hr_f - hr_i
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    """
    Esse é para o caso do jogo durar 24h, já que o
    valor inicial e final vão ser iguais
    """
    duracao = 24
    print(f"O JOGO DUROU {duracao} HORA(S)")
