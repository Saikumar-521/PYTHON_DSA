'''
1.mutable and immutable objects
2.pass by object reference
mutable: list, dict, set
once if an object is created,if we are trying to perfome modfications on the existing object, those modification will be reflected on the same object,then
such type of object are called as mutable objects
ex: list,dict,set
immutable: int,float,string,tuple and fundamental data types
once if an object is created,if we are trying to perfome modfications on the existing object,such type of object are called as immutable objects
'''
# mutable object
l1=[10,20,30]
print(id(l1))
l1.append(40)
print(id(l1))
# immutable object
s1="hello"
print(id(s1))
s1=s1+"python"
print(id(s1))

# string data structure
# collection or sequence or group of characters is called as strong
# string is immutable object
# we can create a string by using single quotes or double quotes or triple quotes and triple double quotes
s1='hello'
s2="hello"
s3='''hello'''
s4="""hello"""
print(s1,type(s1),id(s1))
print(s2,type(s2),id(s1))
print(s3,type(s3),id(s1))
print(s4,type(s4),id(s1))