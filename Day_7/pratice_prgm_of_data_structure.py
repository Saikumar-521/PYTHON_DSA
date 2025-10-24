'''
from collections import deque
def fun(l):
    s=0
    for i in l:
        s+=i
    return s
l=[1,2,3,4,5,6]
print(f'list={l} and sum={fun(l)}')
print(f'list={l} and sum={sum(l)}')
l=[]
print(f'list={l} and sum={fun(l)}')
# print(f'list={l} and sum={sum(l)}')


def fun(l):
    if len(l)==0:
        return 0.0
    s=0
    for i in l:
        s+=i
    return s//len(l)
l=[1,2,3,4,5,6]
print(f'list={l} and avg={fun(l)}')
print(f'list={l} and avg={sum(l)//len(l)}')
l=[]
print(f'list={l} and avg={fun(l)}')
# print(f'list={l} and sum={sum(l)}')


# 03.seperate even and odd elements form list

def even(l):
    l1=[]
    l2=[]
    for i in l:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    print(l)
    print(l1)
    print(l2)
l=[1,2,3,4,5,6,7,8,9,10]
even(l)


def even(l):
    l1=[x for x in l if x%2==0]
    l2=[x for x in l if x%2!=0]
    # for i in l:
    #     if i%2==0:
    #         l1.append(i)
    #     else:
    #         l2.append(i)
    return l1,l2
l=[1,2,3,4,5,6,7,8,9,10]
print(even(l))
even_list,odd_list=even(l)
print(even_list)
print(odd_list)


def even():
    l1=[x for x in range(0,11) if x%2==0]
    l2=[x for x in range(0,11) if x%2!=0]
   
    # print(l)
    # print(l1)
    # print(l2)
    return l1,l2
# l=[1,2,3,4,5,6,7,8,9,10]
even_list,odd_list=even()
print(even_list)
print(odd_list)

# get smaller elements from a list lesser than the given elemnt x
l=[9,10,22,3,4,7,88,5,11,76]
x=10
def smaller(l,small):
    l=[x for x in l if x<=small]
    return l
print(smaller(l,x))

# get the index of given element
l=[9,10,22,3,4,7,88,5,11,76]
x=11
def index_of(l,x):
    ind=0
    for i in l:
        if i==x:
            return ind
        ind+=1
    return 'not found'
print(index_of(l,x))
# predefined function
# x=90 by default the element is not in list return 'None'
def fun(l,x):
    if x in l:
        return l.index(x)
print(fun(l,x))

x=50
def index_of(l,x):
    for i in range(len(l)):
        if x==l[i]:
            return i
    return 'not found'
   
print(index_of(l,x))

# largest and max element in a list
l=[1,5,12,14,3]
def largest(l):
    m=l[0]
    for i in l:
        if m<i:
            m=i
    return m
print(largest(l))
# predefined function
def fun(l):
    return max(l)
print(fun(l))

# find second max/largest element from list
l=[1,5,12,14,3]
def largest(l):
    m=l[0]
    for i in l:
        if m<i:
            m=i
    return m
def sec2(l):
    m=largest(l)
    secm=None
    for i in l:
        if i!=m:
            if secm==None:
                secm=i
            else:
                secm=secm if secm > i else i
    return secm
print(sec2(l))

# second version knowing secound largest element
def fun(l):
    l.sort()
    print(l)
    print(l[-1],'largest element')
    print(l[-2],'second largest element')
fun(l)


# is given list is sorted or not check if it is sorted return true otherwise false
l=[1,2,3,4,5,6,7]
def fun(l):
    i=1
    while i <len(l):
        if l[i]<l[i-1]:
            return False
        i+=1
    return True
print(fun(l)) #true
l=[1,2,3,4,5,6,7,9,8,10]
print(fun(l)) #false

def sorted1(l):
    if l==sorted(l):
        return True
    return False
print(sorted1(l))
l=[1,2,3,4,5,6,7]
print(sorted1(l))


# remove duplicates from list
def fun(l):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s

l=[1,2,3,4,5,2,4,7,6,2,3]
print(l)
print(fun(l))

# using set the insertion order is not preserved




# left rotate a list by one element
# -----------------------------------------------------
# [1,2,3,4,5]------->[2,3,4,5,1]
l=[1,2,3,4,5]
print(l)
l=l[1:] + l[0:1]
print(l) #[2, 3, 4, 5, 1]

# secound version
l=[1,2,3,4,5]
print(l)
l.append(l.pop(0))
print(l)

# third version using function
l=[1,2,3,4,5]
def leftrotationByOne(l):
    n=len(l)
    start=l[0]
    for i in range(1,n):  #for i in range(n-1)
        l[i-1]=l[i]       #l[i]=l[i-1]
    l[n-1]=start
print(l)
leftrotationByOne(l)
print(l)

# leftraotation for k values
l=[1,2,3,4,5,6]
k=3
def lr(l,x):
    n=len(l)
    x=x%n
    l[:]=l[x:]+l[:x]
print('before rotation',l)
lr(l,k)
print('after rotation',l)


# for rightRotation
l=[1,2,3,4,5]
print(l,'before list')
l=l[-1:-2:-1] + l[0:len(l)-1]
print(l,'after list')

l=[1,2,3,4,5]
print(l,'before list')
# l=l[-1:-2:-1] + l[0:len(l)-1]
l.insert(0,l.pop(-1))
print(l,'after list')

l=[1,2,3,4,5]
def rightrotationByOne(l):
    n=len(l)
    end=l[len(l)-1]
    for i in range(1,n-1):
        l[i]=l[i+1]
    l[0]=end
print(l)
rightrotationByOne(l)
print(l)


l = [1, 2, 3, 4, 5,'sai']

def rightrotationByOne(l):
    n = len(l)
    end = l[-1] #same as l[-1]
    for i in range(n-1, 0, -1):  # move from end to start
        l[i] = l[i-1]
    l[0] = end

print("Before rotation:", l)
rightrotationByOne(l)
print("After rotation:", l)


# right rotation for x value:

l=[1,2,3,4,5,6]
k=6
def lr(l,x):
    n=len(l)
    x=x%n
    l[:]=l[-x:]+l[:-x]
print('before rotation',l)
lr(l,k)
print('after rotation',l)


# ep-23 cmplted

l=[1,2,3,4,5]
print(l)
d=int(input('enter number of ratations: '))
l=l[d:]+l[:d]
print(l)


l=[1,2,3,4,5]
print(l)
d=int(input('enter number of ratations: '))
dq=deque(l) 
dq.rotate(-d)#-d indicates left rotation
# l=l[d:]+l[:d]
# print(dq) deque([3, 4, 5, 1, 2])
l=list(dq)
print(l)

# third version
def lr(l,r):
    for i in range(0,d):
        l.append(l.pop(0))


l=[1,2,3,4,5]
print(l)
d=int(input('enter number of ratations: '))
lr(l,d)
print(l)

l=[1,2,3,4,5,6]
k=3
def lr(l,x):
    n=len(l)
    start=l[]
    for i in range(x):
        for j in range(1,n)
print('before rotation',l)
lr(l,k)
print('after rotation',l)

'''
# merge two lists into third list and sort
def fun(l1,l2):
    l=l1+l2
    l.sort()
    return l
l1=[1,2,3,45,2,3]
l2=[4,5,6,7,8,9]
print(fun(l1,l2))

# who has the majority?
# -----------------------------
# given a list of size n and return an element's position which appers greater than n/2 times
# l=[8,3,4,2,8] ----->len(l)=5/2=2 out put 0 or 3 or 4->8
# l=[3,7,4,7,7,5]--------------> n=6/2 =3 ouput:-1
def fun(l):
    n=len(l)
    for i in range(n):
        c=1
        for j in range(i+1,n):
            if l[i]==l[j]:
                c+=1
        if c>n/2:
            # return l[i]
            return i
    return -1
print(fun([2,1,5,2,5,2,2]))
print(fun([3,7,4,7,7,5])) #return -1 why because len(n)/2=3,but the freaquency of 7 element is 3 it most greater than length of list
# assignment for two element have same frequency than return small element


# union of two list
l=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9,10]
def union(l,l2):
    res=[]
    for i in l:
        if i not in res:
            res.append(i)
    for i in l2:
        if i not in res:
            res.append(i)
    return res
print('union of two list',union(l,l2))

# intersection in two element
def intersection(l,l2):
    res=[]
    for i in l:
        if i in l2:
            res.append(i)
    return res
print('intersection of two lists',intersection(l,l2)) #it will print common elements in both list

# difference in the both two list
def differ(l,l2):
    res=[]
    for i in l:
        if i not in l2:
            res.append(i)
    return res
print(l)
print(l2)
print(differ(l,l2))




