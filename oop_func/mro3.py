class O:
  pass
    # print("In O")


class A(O):
    def foo(self):
        print("foo In A")


class B(O):
  pass
    # print("In B")


class C(O):
    def foo(self):
        print("foo In C")


class X(A, B):
  pass
    # print("In X")


class Y(C, B):
  pass
    # print("In Y")


class P(X, Y, C):
  pass
    # print("In P")


aa = P()
aa.foo()

# it prints the lookup order
print(P.__mro__)
print(P.mro())

# Output:
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.N'>, <class '__main__.M'>, <class '__main__.X'>, <class '__main__.O'>, <class 'object'>)
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.N'>, <class '__main__.M'>, <class '__main__.X'>, <class '__main__.O'>, <class 'object'>]

# Giải nghĩa output:
# tìm 1 cái hàm đầu tiên ở class B ko có, típ tìm ở class A, ko có thì tìm ở object
