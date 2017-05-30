'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

def palindrome(n=3):
    limit = int('9' * n) ** 2 #set our limit to the largest square of numbers with n digits
    for i in range(limit, 11, -1): # iterate from limit to 11 - the smallest possible palindrome
        if str(i) == str(i)[::-1]:
            return 'The largest palindrome made from the product of two {}-digit numbers is: {}'.format(n, i)
        
print(palindrome())
