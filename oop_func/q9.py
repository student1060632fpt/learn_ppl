class R(object):
  def foo(self,i):
    print(i*2);

class S1(R):
  pass

class S2(R):
  def foo(self,i):
    print(i+1)

class SS(S1,S2):
  pass

x = SS()
x.foo(3)