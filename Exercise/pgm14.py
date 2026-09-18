class A:
    x = 10
class B(A):
    x = 20
a = A()
b = B()
print(a.x, b.x)
A.x = 30
print(a.x, b.x)