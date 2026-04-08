from funcoes import camel_back_3d, alpine
from algoritmo import algoritmo_genetico

def executar(funcao, nome, execucoes, dimensao, limite, geracoes, tamanho_pop):
    sucessos = 0
    total_nfe = 0

    for _ in range(execucoes):
        _, melhor_valor, nfe = algoritmo_genetico(
            funcao,
            dimensao,
            limite,
            geracoes,
            tamanho_pop
        )

        total_nfe += nfe

        if abs(melhor_valor) < 0.01:
            sucessos += 1

    print(f"\nFunção: {nome}")
    print(f"NFE médio: {total_nfe / execucoes}")
    print(f"Taxa de sucesso: {sucessos}/{execucoes}")


def menu():
    print("=== Algoritmo Genético ===")
    print("1 - Camel Back 3D (CB3)")
    print("2 - Alpine (AP)")

    opcao = input("Escolha a função: ")

    execucoes = int(input("Número de execuções: "))
    dimensao = int(input("Dimensão do problema: "))
    limite = float(input("Limite dos valores: "))
    geracoes = int(input("Número de gerações: "))
    tamanho_pop = int(input("Tamanho da população: "))

    if opcao == "1":
        executar(camel_back_3d, "Camel Back 3D", execucoes, dimensao, limite, geracoes, tamanho_pop)
    elif opcao == "2":
        executar(alpine, "Alpine", execucoes, dimensao, limite, geracoes, tamanho_pop)
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    menu()