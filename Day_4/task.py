import math 
def abs_v1(n):
    if n<0:
        return -n
    else:
        return n

def abs_v2(n):
    return abs(n)
n=int(input('enter the number'))
print(f'orinal value {n} and absolute value {abs_v1(n)}')
print(f'orinal value {n} and absolute value {abs_v2(n)}')

def sum_natural_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
    return sum
def sum_v2(n):
    return n*(n+1)//2

def sum_v3(n):
    if n==1:
        return n
    else:
        return n+sum_v3(n-1)
print(f'orinal value {n} sum of natural numbers is{sum_natural_numbers(n)}')
print(f'version 2 {n} sum of natural numbers is{sum_natural_numbers(n)}')
print(f'version 3 {n} sum of natural numbers is{sum_natural_numbers(n)}')

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def fact_v2(n):
    return math.factorial(n)

def fact_v3(n):
    if n==0:
        return 1
    else:
        return n*fact_v3(n-1)
    
print(f'factorial in v1 {fact(n)}')
print(f'factorial in v2 {fact_v2(n)}')
print(f'factorial in v3 {fact_v3(n)}')

def digits_v1(n):
    c=0
    while n>0:
        x=n%10
        c+=1
        n=n//10
    return c
        



n1=int(input('enter number for digit count'))
print(f'{digits_v1(n1)}')