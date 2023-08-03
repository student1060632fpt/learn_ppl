# Let lst be a list of integer and n be any value, use recursive approach to write function dist(lst,n) that returns the list of pairs of an element of lst and n.

def dist(lst,n):
  if len(lst) == 0: return []
  print(lst[-1]) 
  # lst[-1] sẽ lấy đc phần tử cuối
  # lst[:-1] sẽ xóa đc phần tử cuối
  return dist(lst[:-1],n) + [(lst[-1],n)]

print(dist([1,2,3],4))
# [(1, 4),(2, 4),(3, 4)]
