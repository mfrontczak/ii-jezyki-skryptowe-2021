# https://pl.wikipedia.org/wiki/Sito_Eratostenesa
import math

N = 1000000

sito = [True for _ in range(N)]
for i in range(2, int(math.sqrt(N))):
    if sito[i] is True:
        for j in [x*i for x in range(2, N) if x*i < N]:
            sito[j] = False

# https://docs.python.org/3/library/functions.html#enumerate 
for liczba, czy_pierwsza in enumerate(sito[2:], start=2):
    if czy_pierwsza is True:
        print(f"{liczba:7d} jest liczbą pierwszą.")
