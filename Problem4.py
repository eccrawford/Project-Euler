'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.


First, I need a function that determines if a number is a palindrome.
This is simple enough, using modulus and checking to see if the input
is equal to the reversed output.

Starting from 999, I can multiply the two numbers and update a
largestPalindrome variable that keeps track of the palindromes I find,
and returns the largest one.
'''

def isPalindrome(x):
    num = x
    reverse = 0
    while(num > 0):
        digit = num%10
        reverse = reverse*10 + digit
        num = num/10
    if x == reverse:
        return True
    else:
        return False

def Problem4():
    num1 = 999
    largestPalindrome = 0
    while (num1 >= 100):
        num2 = 999
        while (num2 >= num1):
            product = num1*num2
            if product <= largestPalindrome: #otherwise it will return the first palindrome it finds
                break
            if (isPalindrome(product)):
                largestPalindrome = product
            num2 -=1
        num1 -= 1
    return largestPalindrome
            
print Problem4() #906609
