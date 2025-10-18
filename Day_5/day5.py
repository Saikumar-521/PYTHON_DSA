import math
def power_v1(x,y):
    r=1
    for i in range(1,y+1):
        r=r*x
    return r
print(power_v1(2,3))

def power_v2(x,y):
    return x**y
print(power_v2(2,3))

def power_v3(x,y):
    return int(math.pow(x,y))
print(power_v3(2,4))

# sum of digits
def sum_v1(n):
    s=0
    while n!=0:
        d=n%10
        s=s+d
        n=n//10
    return s
def sum_v2(n):
    return sum(int(i) for i in str(n))


n=int(input('enter a number'))
print(sum_v1(n))
print(sum_v2(n))

# sum of prime numbers
def sum_of_prime_v1(n):
    s=0
    while n!=0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:
            s=s+d
        n=n//10
    return s

def sum_of_prime(n):
    return sum(int(i) for i in str(n) if i in "2357")
print(sum_of_prime_v1(2476567430))
print(sum_of_prime(235710984))


def prime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    return f==2

def prime_v2(n,i):
    if i==1:
        return True
    elif n%i==0:
        return False
    else:
        return prime_v2(n,i-1)

print(prime(7))
print(prime_v2(7,7//2))


# all divisors of n
def divisors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

print(divisors(20))

# perfect number:n----------->sum of its factors excluding that number should be equal to n
# 6=======>1,2,3,(6)-------->1+2+3=6 true
# 10------>1,2,5,10------>1+2+5=8------->false


def divisors(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return l

def isperfect(n):
    l=divisors(n)
    return n==sum(l)


print(isperfect(6))


# amstrong number
# 123-------->1^3+2^3+3^3=1+8+27=36=---------->123==36 False
# 153 ------->1^3 + 5^3 + 3^3 = 1+125 +27=153--------->153==153 true
def armstong(n):
    s=0
    t=n
    while n!=0:
        d=n%10
        s=s+d**3
        n=n//10
    return s==t

print(armstong(123))
print(armstong(153))

for i in range(1,1000+1):
    if armstong(i):
        print(i)


# strong number: sum of given digit of factorial numbers is  equal to given number than it is strong number
# 123----->1!+2!+3!=1+2+6=9------->false
# 145--->1!+4!+5! =1+24+120-->145=145  true

import math
def strong(n):
    s=0
    t=n
    while n!=0:
        d=n%10
        s=s+math.factorial(d)
        n=n//10
    return s==t

for i in range(1,1000+1):
    if strong(i):
        print(i)


# fibonnic sequence:by adding previous two numbers
# 0 1 1 2 3 5
def fib(n):
    l=[]
    a=0
    b=1
    l.append(a)
    l.append(b)
    for i in range(n-2):
        c=a+b
        l.append(c)
        a=b
        b=c
    return l
print(fib(5))

# trib sequence:adding previous 3 numbers
# 0 1 2 3 6 11 20 37
def fib(n):
    l=[]
    a=0
    b=1
    c=2
    l.append(a)
    l.append(b)
    l.append(c)
    for i in range(n-3):
        d=a+b+c
        l.append(d)
        a=b
        b=c
        c=d
    return l
print(fib(8)) #[0, 1, 2, 3, 6, 11, 20, 37]

# ep-13 cmplt
