# Let lst be a list of integer and n be an integer, use high-order function approach to write function lessThan(lst,n) that returns the list of all numbers in lst less than n.
def lessThan(lst, n):
    return [x for x in lst if x < n]


print(lessThan([1, 2, 3, 4, 5], 4))
# [1,2,3]
