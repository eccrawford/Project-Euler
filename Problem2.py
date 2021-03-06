#The Problem:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

num1 = 0
num2 = 1
evenSum=0
limit = 4000000

while ((num1 + num2) < limit):
    sum = num1 + num2
    if sum%2 == 0:
        evenSum+=sum
    num1=num2
    num2=sum
        
print "The sum of even Fibonacci terms under 4,000,000 is", evenSum;
