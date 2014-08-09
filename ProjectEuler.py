__author__ = 'joefalkson'


print("Hello world")

'''
Project Euler Problem 1
Find the sum of all the multiples of 3 or 5 below 1000.
'''

total = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        total += i
    i += 1
print("total is " + str(total))


'''
Project Euler Problem 2
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''


