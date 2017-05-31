'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

from math import floor
from math import sqrt

def prime_factors(n=600851475143):
    x = n
    factors = []
    if x % 2 == 0:
        factors.append(2)
        x /= 2
    for i in range(3, floor(sqrt(x)), 2): #
        if  x % i == 0:
            factors.append(i)
            x /= i
    print("The largest prime factor of {} is {}.".format(n, max(factors)))
