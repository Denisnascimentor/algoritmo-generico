import math


def camel_back_3d(vetor):
    x, y = vetor

    termo1 = 2 * x**2
    termo2 = -1.05 * x**4
    termo3 = (x**6) / 6
    termo4 = x * y
    termo5 = y**2

    return termo1 + termo2 + termo3 + termo4 + termo5



def alpine(vetor):
    return sum(abs(x * math.sin(x) + 0.1 * x) for x in vetor)
    