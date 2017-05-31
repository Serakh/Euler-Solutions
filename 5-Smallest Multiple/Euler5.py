'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

from math import factorial

def mult(n=10):
  multiples = list(range(2, n+1))
  for i in range(2*n, factorial(n),  n):
    if all(i % j == 0 for j in multiples):
      return i
