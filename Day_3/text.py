def even_odd_v1(n):
    return n%2==0
def evenorodd(n):
    return (n&1)==0
n=int(input('enter a number'))
print(even_odd_v1(n))
print(evenorodd(n))
print('3'*10)

# four and five among maximum number
def max_v1(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        return a
    elif b>c and b>d and b>e:
        return b
    elif c>d and c>e:
        return c
    elif d>e:
        return d
    else:
        return e
def max_v2(a,b,c,d,e):
    return a if a>b and a>c and a>d and a>e else b if b>c and b>d  and b>e else c if c>d and c>e else d if d>e else e
def max_v3(a,b,c,d,e):
    return max(a,b,c,d,e)

a=int(input("enter a value "))
b=int(input("enter a value "))
c=int(input("enter a value "))
d=int(input("enter a value "))
e=int(input("enter a value"))
print(max_v1(a,b,c,d,e))
print(max_v2(a,b,c,d,e))
print(max_v3(a,b,c,d,e))

# swaping the two numbers
def swap(a,b):
    print(f"original numbers {a} and {b}")
    a,b=b,a
    print(f"after swaping {a} and {b}")

def swap_v1(a,b):
     print(f"original numbers {a} and {b}")
     t=a
     a=b
     b=t
     print(f"after swaping {a} and {b}")

def swap_v2(a,b):
     print(f"original numbers {a} and {b}")
     a=a+b
     b=a-b
     a=a-b

     print(f"after swaping {a} and {b}")

def swap_v3(a,b):
     print(f"original numbers {a} and {b}")
     a=a*b
     b=a//b
     a=a//b

     print(f"after swaping {a} and {b}")

def swap_v4(a,b):
     print(f"original numbers {a} and {b}")
     a=a^b
     b=a^b
     a=a^b

     print(f"after swaping {a} and {b}")

def swap_v5(a,b):
     print(f"original numbers {a} and {b}")
     a=a+b-(b:=a) #wallrus operator during excution the value is assinged
     print(f"after swaping {a} and {b}")

print(swap(a,b))
print(swap_v1(a,b))
print(swap_v2(a,b))
print(swap_v3(a,b))
print(swap_v4(a,b))
print(swap_v5(a,b))
