# lendo 4 notas obtidas por um aluno
n1, n2, n3, n4 = input().split()

# transformando as notas lidas em valores de ponto flutuante
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

# calculando a média
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

# imprimindo a média na tela
print(f"Media: {media:.1f}")

# Criando uma operação condicional com a média do aluno para ver qual a situação final dele
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    # Caso o aluno fique de exame, pede-se a nota do exame que ele fez, para assim, recalcular sua média (media_final)
    print("Aluno em exame.")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    # Criando outra outra operação condicional, para verificar qual a situação do aluno depois de sua média (media_final) ser recalculada
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
