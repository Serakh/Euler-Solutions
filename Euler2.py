'''Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.'''

def e_fib(n=4000000):
    fib = [1, 2]
    even = [2]
    current = sum(fib[-2:])
    while current <= n:
        fib.append(current)
        if current % 2 == 0:
            even.append(current)
        current = sum(fib[-2:])
    print("The sum of even fibonacci numbers under {} is {}.".format(n, sum(even)))
