# Various ways to get keys of Dictionary
d = {'a':1,
     'b':2,
     'c':3,}
x = d.keys()
print([k for k in x])

all = list(d.keys())
print(all)

print()

x1 = [*d.keys()]
print(x1)
x2 = [*d]
print(x2)

print()

# Multiple Inheritance in Python (Diamond Problem):
class A:
    def ab(self):
        print('a')
    
class B(A):
    def ab(self):
        print('b')

class C(A):
    def ab(self):
        print('c')
    
class D(B,C):
    pass

d = D()
d.ab()

print()

