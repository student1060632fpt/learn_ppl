class Num:
  # print("num nè")
  def __init__(self,x):
    self.x = x
    print("num init nè",self.x)

class Add:
  # print("Add nè")
  def __add__(self,other): # đây là hàm python cung cấp
    print("Add nè", other.x)
    return self.x + other.x

class Mul:
  # print("mul nè")
  def __mul__(self,other):
    print("mul nè",other.x)
    return self.x*other.x

class Num1(Num,Add): 
  print("num1 nè")
  pass
class Num2(Num,Mul):
  print("num2 nè")
  pass

x = Num1(4)
y = Num2(5)
print(x + y, y * x)
# Fill in the blanks such that expressions x + y and y * x are valid while x * y and y + x are invalid
# điền sao cho x + y và y * x hợp lệ
# còn x * y và y + x là ko hợp lệ