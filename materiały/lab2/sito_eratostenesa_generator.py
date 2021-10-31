import math

N = 1000000

sito_gen = (i for i in range(2, N) if not any(True for j in range(2, int(math.sqrt(i))) if i % j == 0))

for pierwsza in sito_gen:
    print(f"{pierwsza:7d} jest liczbą pierwszą.")
