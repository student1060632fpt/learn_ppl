# Python program to show the order: https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
# in which methods are resolved

class A:
	def foo(self):
		print(" In class A")
class B(A):
	def foo(self):
		print(" In class B")

# classes ordering
class C(B):
	def __init__(self):
		print("Constructor C")

fo = B()

# it prints the lookup order
# print(C.__mro__)
# print(C.mro())

print(B.__mro__)
print(B.mro())

# Output: 
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# giải nghĩa
# tìm 1 cái hàm đầu tiên ở class B ko có, típ tìm ở class A, ko có thì tìm ở object 
