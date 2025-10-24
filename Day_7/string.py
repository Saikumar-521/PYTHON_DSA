'''
shallow copy and deep copy in python
once if copy of list object got  created,if it contains any nested list objects,then
if we perform any modifications on nested list object,those modifications will be reflected for both list objects,i.e nested list objects are
shared.this type of operation is called as shallow copy or normal copy

ex:

shallow copy:
defination:copying of object where only reference of nested objects are copied

example:
import copy
original_list=[1,2,[3,4],5]
shallow_copied_list=copy.copy(original_list)
print("Before modification:")
print("original_list:",original_list)
print("shallow_copied_list:",shallow_copied_list)
#modifying nested list object in original_list
original_list[2][0]=99
print("After modification:")
print("original_list:",original_list)
print("shallow_copied_list:",shallow_copied_list)


deep copy:
once if copy of list object got  created,if it contains any nested list objects,then
if we perform any modifications on nested list object,those modifications will be reflected for only one list objects,i.e nested list objects are not
shared.this type of operation is called as deep copy.

or

defination:copying of object where new nested objects are created
example:
import copy
original_list=[1,2,[3,4],5]
deep_copied_list=copy.deepcopy(original_list)
print("Before modification:")
print("original_list:",original_list)
print("deep_copied_list:",deep_copied_list)
#modifying nested list object in original_list
original_list[2][0]=99
print("After modification:")
print("original_list:",original_list)
print("deep_copied_list:",deep_copied_list)
'''

import copy
import math
original_list=[1,2,[3,4],5]
shallow_copied_list=copy.copy(original_list)
print("Before modification:")
print("original_list:",original_list)
print("shallow_copied_list:",shallow_copied_list)
#modifying nested list object in original_list
original_list[2][0]=99
print("After modification:")
print("original_list:",original_list)
print("shallow_copied_list:",shallow_copied_list)

original_list=[1,2,[3,4],5]
deep_copied_list=copy.deepcopy(original_list)
print("Before modification:")
print("original_list:",original_list)
print("deep_copied_list:",deep_copied_list)
#modifying nested list object in original_list
original_list[2][0]=99
print("After modification:")
print("original_list:",original_list)
print("deep_copied_list:",deep_copied_list)


'''list comprehension
list comprehension is a concise way to create lists in python.it provides a syntactic way to generate lists based on existing iterables like lists,tuples,or ranges.
sytax1:[expression for item in iterable]
sytax2:[expression for item in iterable if condition]'''

# find factorial of each list number using list comprehension
import math
numbers=[1,2,3,4,5]
# factorials=[1 if n==0 else n*factorials[n-1] for n in range(6)]
factorials=[math.factorial(n) for n in numbers]

print("Factorials using list comprehension:",factorials)
# without using math module
# factorials_without_math=[1 if n==0 else n*factorials_without_math[n-1] for n in range(6)]
# print("Factorials without using math module:",factorials_without_math)

ol=[1,2,3,4,5,6,7,8,10]
nl=[i  for i in ol if i%2==0]
nl1=[i  for i in ol if i%2!=0 ]
print(ol)
print(nl)
print(nl1)
'''
common functions on list
len(list) length of list
max(l)  max element of list
min(l)  max element of list
sorted(l)  sorted list with all elements in asc order
sorted(l,reverse=true) sorted list with all elements in desc order
sum(l) sum of all element


-------------------------------------------------
list methods:
append():adds an element at the end of the list
extend():adds all elements of a list to another list, add only iterable objects
insert():inserts an element at the specified position
remove():removes the first occurrence of a specified element
pop():removes and returns the element at the specified position (or last element if index not specified)
index():returns the index of the first occurrence of a specified element
clear():removes all elements from the list
count():returns the number of occurrences of a specified element
reverse():reverses the order of elements in the list
sort():sorts the elements of the list in ascending order (or descending order if specified)
sorted():returns a new sorted list from the elements of the original list
copy():returns a shallow copy of the list

'''
# sort the list based on length of string
words=["apple","banana","kiwi","cherry","blueberry","fig","grape"]
sorted_words=sorted(words,key=len)
print("Original words list:",words)
print("Sorted words list based on length:",sorted_words)

# sort the list based on alphabetical order and length of string
sorted_words_alpha_len=sorted(words,key=lambda x:(x.lower(),len(x)))
print("Sorted words list based on alphabetical order and length:",sorted_words_alpha_len)

# sort the list based on alphabetical order and length of string without lambda
def sort_key(x):
    return (x.lower(),len(x))
sorted_words_alpha_len_no_lambda=sorted(words,key=sort_key)
print("Sorted words list based on alphabetical order and length without lambda:",sorted_words_alpha_len_no_lambda)

'''
tuple: data structure creation
creation;
it is a group of objects of different types.
it is represented by using()
it is not growable
immutable object
it is index based data structure
slicing is allowed
insertio order is preserved
duplicates are allowed.

---------------------
creation of tuple object
1.()
2.(obj1,obj2,obj3,---)
3.tuple()
4.(obj1,)--->tuple creation,if (obj)---> this is integer
5.input with tuple()
6.eval()

nested tuple objects:
a tuple object within another tuple object is called as nested tuple

tuple aliasing:
assigning anew reference variable for an existing tuple object is called as tuple aliasing

tuple cloning is no:

'''
t=(1,2,3,4)
t1=t  #t.copy(t1) not working if import copy and use copy than works and don't allow the shallow copy and deep copy
print(t)
print(t1)

print(t is t1)

'''

tuple specific methods:
index(object):
it returns location of the given object

count(object):
it returns number of occerences of the given object

tuple packing and tuple unpacking:
---------------------------------------
converting individual objects into tuple is called as tuple packing.
converting tuple into individual objects is called as tuple unpacking.
'''
# tuple packing
a=1
b=2
c=3
t=a,b,c
print(type(a),a) #class< 'int'> 1
print(type(b),b) #class< 'int'> 2
print(type(c),c) #class< 'int'> 3

print(type(t),t) #<class 'tuple'> (1,2,3)


# tuple unpacking
t=(10,20,30,40)
w,x,y,z=t
print(w,type(w)) #class < 'int'> 10
print(x,type(x)) #class < 'int'> 20
print(y,type(y)) #class < 'int'> 30
print(z,type(z)) #class < 'int'> 40

print(t,type(t))

a=('hello')
print(a,type(a))

b=('hello',)
print(b,type(b))



'''
set data structure creation
introduction:
it is a group of objects of different types.it must be (immtubale objects)
it is represented by using{}
it is  growable (add/remove)
mutable object
it is  not index based data structure
slicing is  not allowed
insertio order is not preserved
duplicates are  not allowed.

---------------------
creation of tuple object
1.set()
2.{obj1,obj2,obj3,---}
3.input with set function
4.eval()



common functions on list
len(list) length of list
max(l)  max element of list
min(l)  max element of list
sum(l) sum of all element

set specific methods:
----------------------
add
remove

'''
s={1,2,(3,4)}
print(s) #it will excutes
# s={1,2,[4,55]}
# print(s) unhashable type: 'list'
# s={1,2,{3,4}}
# print(s)  TypeError: unhashable type: 'set'

# add()
s.add((3,45,6))
s.add('sai')
print(s)

# remove(object): if there is o object then return error
s.remove('sai')
print(s)
# s.remove('sai kumar')
# print(s) KeyError: 'sai kumar'


# discard()
s.discard(1)
print(s)
s.discard(1)
print(s) #no errors rasies


'''
dictionary data structure or dict data structure
1.collection of individual object------>str,list,tuple,set
collection of key-value pairs are called as dictionary or dict
it is represented by using {}
<class dict>

index concept is not allowed but keys are acting as index
(duplicate keys are not allowed but values can be duplicated)


'''
d={1:'sai',2:'kuamr',3:'yadavs'}
print(d)
print(type(d))
d[2]='ram'
print(d)

'''
dict methods()
-----------------------------
d[key]=value
it add key and value pair into the existing dict.

'''
d={'sai':[1,2,3,4]}
print(d)
# d={[1,2,3]:'sai'} TypeError: unhashable type: 'list' ,the keys only immutable type
print(d)
d={(1,2,3):'sai'}
print(d)
d[(1,2,3)]='kumar'
print(d)
d.clear()
print(d)

d={1:'sai',2:'kumar',3:'yadavs',4:'emledu bro'}
print(d.keys()) #dict_keys([1, 2, 3, 4])
print(d.values())  #dict_values(['sai', 'kumar', 'yadavs', 'emledu bro'])
print(d.items())   #dict_items([(1, 'sai'), (2, 'kumar'), (3, 'yadavs'), (4, 'emledu bro')])

'''
get(key,default):
it returns a value associated with given key,if key is not there than return the default value.

dictionary comprehension:
easiest way to create dict is nothing dict comprehension.
syntax1:{key_expr:Val_expression for i in sequence}

'''
d={i:i*i for i in range(1,11)}
print(d)

def isprime2(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    return f==2

d1={i:math.factorial(i) for i in range(1,11) if not isprime2(i)}
print(d1)
