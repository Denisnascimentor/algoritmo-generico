import random

def algoritmo_genetico(funcao, dimensao=3, limite=5, geracoes=100, tamanho_pop=50):
    # Inicializa a população (apenas os vetores/cromossomos)
    populacao = [
        [random.uniform(-limite, limite) for _ in range(dimensao)]
        for _ in range(tamanho_pop)
    ]

    total_nfe = 0
    pop_avaliada = []

    # Avalia a população inicial e guarda o fitness
    for ind in populacao:
        pop_avaliada.append({'cromossomo': ind, 'fitness': funcao(ind)})
        total_nfe += 1

    for _ in range(geracoes):
        nova_populacao = []

        for _ in range(tamanho_pop):
            # Seleção por torneio usando o fitness já calculado
            grupo1 = random.sample(pop_avaliada, 3)
            grupo2 = random.sample(pop_avaliada, 3)

            pai1 = min(grupo1, key=lambda x: x['fitness'])['cromossomo']
            pai2 = min(grupo2, key=lambda x: x['fitness'])['cromossomo']

            # Crossover aritmético
            beta = random.random()
            filho = [
                beta * a + (1 - beta) * b
                for a, b in zip(pai1, pai2)
            ]

            # Mutação gaussiana
            filho = [
                gene + random.gauss(0, 1) * 0.1
                for gene in filho
            ]

            nova_populacao.append(filho)

        # Avalia toda a nova população gerada
        pop_avaliada = []
        for ind in nova_populacao:
            pop_avaliada.append({'cromossomo': ind, 'fitness': funcao(ind)})
            total_nfe += 1

    # Busca o melhor da última geração (usando o valor já guardado)
    melhor_individuo = min(pop_avaliada, key=lambda x: x['fitness'])
    
    return melhor_individuo['cromossomo'], melhor_individuo['fitness'], total_nfe