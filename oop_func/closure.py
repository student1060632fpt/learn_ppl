def power(y):
  print("power: y = ",y)
  def inner(x):
    print("inner: x = ",x)
    return x**y
  print(inner)
  return inner
square = power(2)

print("square = ",square(5))