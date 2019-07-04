# Check if the number is prime
def isPrime(n):
    f=True
    for i in range (2,n):
        if n%i==0:
            return False
    return f


 # Factorial of Number
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
#n=int(input())
#print(factorial(n))


def upper(S):
    return S.swapcase()