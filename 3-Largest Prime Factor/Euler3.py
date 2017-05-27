'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

from math import floor

def prime_factors(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        n /= 2
    for i in range(3, math.floor(sqrt(n)), 2): #
        if  n % i == 0:
            factors.append(i)
            n /= i
    print(factors)