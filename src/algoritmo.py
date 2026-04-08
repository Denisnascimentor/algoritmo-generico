import random

def algoritmo_genetico(funcao, dimensao=2, limite=5, geracoes=100, tamanho_pop=50):
    populacao = [
        [random.uniform(-limite, limite) for _ in range(dimensao)]
        for _ in range(tamanho_pop)
    ]

    total_avaliacoes = 0

    for _ in range(geracoes):
        nova_pop = []

        for _ in range(tamanho_pop):

            candidatos1 = random.sample(populacao, 3)
            candidatos2 = random.sample(populacao, 3)

            pai1 = min(candidatos1, key=funcao)
            pai2 = min(candidatos2, key=funcao)


            fator = random.random()
            filho = [
                fator * a + (1 - fator) * b
                for a, b in zip(pai1, pai2)
            ]


            filho = [
                gene + random.gauss(0, 1) * 0.1
                for gene in filho
            ]

            nova_pop.append(filho)
            total_avaliacoes += 1

        populacao = nova_pop

    melhor = min(populacao, key=funcao)
    return melhor, funcao(melhor), total_avaliacoes