n = int(input())

saque = []
bloqueio = []
ataque = []

saque_succ = []
bloqueio_succ = []
ataque_succ = []

for i in range(n):
    nome = input()

    try_s, try_b, try_a = map(int, input().split())
    saque.append(try_s)
    bloqueio.append(try_b)
    ataque.append(try_a)

    total_saque = sum(saque)
    total_bloqueio = sum(bloqueio)
    total_ataque = sum(ataque)

    succ_s, succ_b, succ_a = map(int, input().split())
    saque_succ.append(succ_s)
    bloqueio_succ.append(succ_b)
    ataque_succ.append(succ_a)

    total_saque_succ = sum(saque_succ)
    total_bloqueio_succ = sum(bloqueio_succ)
    total_ataque_succ = sum(ataque_succ)

    p_saque = (total_saque_succ * 100) / total_saque
    p_bloqueio = (total_bloqueio_succ * 100) / total_bloqueio
    p_ataque = (total_ataque_succ * 100) / total_ataque

print("Pontos de Saque: {:.2f} %.".format(p_saque))
print("Pontos de Bloqueio: {:.2f} %.".format(p_bloqueio))
print("Pontos de Ataque: {:.2f} %.".format(p_ataque))
