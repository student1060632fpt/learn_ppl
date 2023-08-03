# Let lst be a list of integer and n be an integer, use recursive approach to write function lessThan(lst,n) that returns the list of all numbers in lst less than n.

def lessThan(lst, n):
    if (len(lst) == 0):
        return []
    return lessThan(lst[:-1],n) + ([lst[-1]] if lst[-1] < n else [])

# def lessThan(lst, n):
#     if not lst:
#         return []
    
#     head, *tail = lst
#     if head < n:
#         return [head] + lessThan(tail, n)
#     else:
#         return lessThan(tail, n)

print(lessThan([1, 2, 3, 4, 5], 4))
# [1,2,3]
