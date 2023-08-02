# Python program to show the order: https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
# in which methods are resolved

class M:
	def foo(self):
		print(" In M")
class N:
	def foo(self):
		print(" In N")
class X:
	def foo(self):
		print(" In X")
class O:
	def foo(self):
		print(" In O")


class A(M and X and O):
	def foo(self):
		print(" In A")

class B(N and M and O):
	def foo(self):
		print(" In B")

# classes ordering
class C(A and B):
	def __init__(self):
		print("Constructor C")


aa = C()
aa.foo()

# it prints the lookup order
print(C.__mro__)
print(C.mro())

# Output: 
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.O'>, <class 'object'>)
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.O'>, <class 'object'>]

# Giải nghĩa output:
# tìm 1 cái hàm đầu tiên ở class B ko có, típ tìm ở class A, ko có thì tìm ở object 
