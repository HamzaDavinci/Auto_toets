import math
import random

def tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand):
    afstand = kilometers_per_liter * tankinhoud
    tankbeurten = math.ceil(afstand / te_rijden_afstand)

    return tankbeurten

print(tanken(10, 8, 80))
for _ in range(9):
    print(tanken(10, random.randint(0,10), random.randint(0,100)))