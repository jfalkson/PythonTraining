__author__ = 'joefalkson'

##here we look at the probabilities of various outcomes
##recall binomial probability is (n choose k) * p^k * q ^(n-k) where
#p is the probability of success and q is the probability of failure.


def factorial(n):
    count = n
    ans = n
    if n == 0:
        return 1

    while count > 1:
        count-=1
        ans = ans*count
    return ans

factorial(3)

def binomialprob(p, q, n, k):
    return