# Lendo a data inicial do evento
começo, dia_i = input().split()
dia_i = int(dia_i)
hora_i, min_i, seg_i = map(int, input().split(" : "))

# Lendo a data final do evento
fim, dia_f = input().split()
dia_f = int(dia_f)
hora_f, min_f, seg_f = map(int, input().split(" : "))

# Convertendo o tempo para segundos
minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = seg_i + min_i * minuto_seg + hora_i * hora_seg + dia_i * dia_seg
f = seg_f + min_f * minuto_seg + hora_f * hora_seg + dia_f * dia_seg

# Calculando a duração
# Transformando no formato pedido (dia, hora, minutos, segundos)
if i < f:
    duracao = f - i
    dias = int(duracao // dia_seg)
    duracao = duracao % dia_seg
    horas = int(duracao // hora_seg)
    duracao = duracao % hora_seg
    minutos = int(duracao // minuto_seg)
    duracao = duracao % minuto_seg
    segundos = duracao

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
