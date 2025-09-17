'''
single Linked List operations:
e

---------------------------------
1.inserting the data first
inserting the data last
inserting the data at position
sorted insertion asc/desc
traversing and displaying
size or length of list
reverse list
searching
deleting from first
deleting from last
delete from position
deleting element
deleting elements
deleting duplicates
copy of original list
comparing teo list objects
finding nth node from begining and ending

'''
def add_first(self,value):
    newnode=self.node(value,None)
    if self.head==None:
        self.head=newnode
        return
    newnode.next =self.head
    self.head=newnode
def addL(l):  
    s=0 #it is version1
    for i in l:
        s+=i
    return s
def added(l):
    return sum(l) #it is version2

l=[11,22,33,44,55]
print(addL(l))
print(added(l))

# maximum of two numbers
def maxfun_version1(a,b):
    return max(a,b)
def maxfun_version2(a,b):
    return a if a>b else b

a=int(input())
b=int(input())
print("max value by using version1:",maxfun_version1(a,b))
print("max value by using version1:",maxfun_version2(a,b))

#minmum of two numbers
# complexity:
'''
complexity of an algorithm is the amount of time or space reqired by the algorithm or program to the
inputs and produce output.

1.time complexity
2.space complexity
time-complexity:
the amount of time taken by the algorithm to process the inputs is called as time complexity which is measured by using T(n)

space complexity:
-------------------
the amount of space taken by the algorithm to process the inputs is called as sapce complexity,which is measured by using S(n)

Asymptotic notations:
----------------------
Bog-oh notation:O(n)
Omega notatin :W(n)
Theta notation: 0(n)



all these programs or algorithms are classified into three types

1.worst case complexity
2.average case complexity
3.best case complexity
'''