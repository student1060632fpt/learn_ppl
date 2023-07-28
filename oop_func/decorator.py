def log_decorator(func):
    def inner(*arg):
      print(func.__name__ + " is run")
      res = func(*arg)
      print(func.__name__ + " is finish")
      return res
    return inner

@log_decorator
def foo(x,y):
  return x*y
print(foo(3,4))