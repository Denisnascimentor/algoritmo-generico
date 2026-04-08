import math

def sphere(vetor):
    return sum(valor**2 for valor in vetor)

def rastrigin(vetor):
    tamanho = len(vetor)
    return 10 * tamanho + sum(
        valor**2 - 10 * math.cos(2 * math.pi * valor)
        for valor in vetor
    )