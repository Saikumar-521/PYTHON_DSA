'''
algorithm:
step by step process for solving any problem is called as an algorithm.

flowchart:
diagramitcal or pictorial represtantion of the algorithm is know flow chart
advantages of alogrithm/flowchart
1.problem will be simmplified.
2.easy to understand problem statement.
easy to implement
4.we will get a format/template /pattern to solve the problem

properties of algorithm
1.zero or more inputs
2.one or more outputs.
3.deterministic-->same ooutput for same input again and again
4.correct
5.terminate at finate steps base condition
6.efficient
'''
#1.wpp to read a string and convert all even indexed values into uppercase
# def myFun(s):
#     l=list(s.lower())
#     # l1=[]
#     for i in range(len(l)):
#         if i%2==0:
#             l[i]=l[i].upper()
#     return ''.join(l)
        

# s=input('enter any string')
# print(s)
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
# print(myFun(s))
s="sai Kumar"
print(s.capitalize())
print(s.casefold())
# print(s.center())
print(s.encode())
print(s.endswith('a'))
print(s.find("a"))
print(s.format())
# print(s.format_map())
print(s.index('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isdigit())
print(s.isidentifier())
print(s.islower())
print(s.isspace())