def dist(lst,n):
  return list(map(lambda x: (x,n),lst))

print(dist([1,2,3],4))
# [(1, 4),(2, 4),(3, 4)]