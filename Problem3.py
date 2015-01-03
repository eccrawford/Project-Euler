#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?


'''
It's tempting to try and loop through the given number and update
a variable after every new prime factor is found. It's possible, but since the
number is quite large, this would take awhile.
The fundamental theorem of arithmetic states that every number greater
than 1 is either a prime number, or can be written as a factor of prime numbers.
This theorem is what my solution is based on.
I update the dividend and the largestPrime variable every time
a factor is found. When the square of the divisor is bigger than the dividend
(also the remainder) this means that the remainder is the largest prime.

As an example: If the given number was 35, this would be the output
Starting with divisor=2:
divisor=3
divisor=4
divisor=5
(35%5 = 0! So 5 is a factor, and we can update our dividend)
dividend=7
largestPrime=5
(5*5=25, which is greater than 7, so we  break out of the loop)
If the dividend is greater than the last divisor, we know this number
is the actual largest prime factor.
'''

num=600851475143
dividend=num
divisor=2
largestPrime=0

while divisor*divisor <= dividend:
    if dividend%divisor == 0:
        dividend = dividend/divisor
        largestPrime = divisor
    else:
        divisor+=1
if dividend > largestPrime:
    largestPrime=dividend
print "The largest prime number is", largestPrime;

