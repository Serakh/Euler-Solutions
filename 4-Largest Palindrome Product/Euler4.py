'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

def palindrome(digits=3):
    greatest = int('9' * digits)
    least = int('1' + '0' * (digits-1)) 
    for i in range(greatest ** 2, least ** 2, -1):
        if str(i) == str(i)[::-1]:
            for j in range(greatest, least, -2):
                if i % j == 0 and len(str(int(i/j))) == digits:
                    return 'The largest palindrome made from the product of two {}-digit numbers is {} which is a product of {} and {}.'.format(digits, i, j, int(i/j))
        
print(palindrome())
