# Lendo o horário de um jogo
hr_i, min_i, hr_f, min_f = map(int, input().split())

min_i_total = (hr_i * 60) + min_i
min_f_total = (hr_f * 60) + min_f

# Calculando a duração do jogo
if min_i_total >= min_f_total:
    duracao = (24 * 60 - min_i_total) + min_f_total
    duracao_hr = duracao // 60
    duracao_min = duracao % 60

    print(f"O JOGO DUROU {duracao_hr} HORA(S) E {duracao_min} MINUTO(S)")

else:
    duracao = min_f_total - min_i_total
    duracao_hr = duracao // 60
    duracao_min = duracao % 60

    print(f"O JOGO DUROU {duracao_hr} HORA(S) E {duracao_min} MINUTO(S)")
