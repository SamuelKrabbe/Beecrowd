# Calculando o salário de um funcionário
sal = float(input())

# Calculando o reajuste do salário baseado no seu sarário inicial
if sal >= 0 and sal <= 400:
    novo_sal = sal * 1.15
    reajuste = sal * 0.15

    print(f"Novo salario: {novo_sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {15} %")

elif sal >= 400.01 and sal <= 800:
    novo_sal = sal * 1.12
    reajuste = sal * 0.12

    print(f"Novo salario: {novo_sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {12} %")

elif sal >= 800.01 and sal <= 1200:
    novo_sal = sal * 1.10
    reajuste = sal * 0.10

    print(f"Novo salario: {novo_sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {10} %")

elif sal >= 1200.01 and sal <= 2000:
    novo_sal = sal * 1.07
    reajuste = sal * 0.07

    print(f"Novo salario: {novo_sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {7} %")

else:
    novo_sal = sal * 1.04
    reajuste = sal * 0.04

    print(f"Novo salario: {novo_sal:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {4} %")
