# Use recursive approach to write a function lstSquare(n:Int) that returns a list of the squares of the numbers from 1 to n?

def lstSquare(size):
    if (size == 0):
        return []
    return lstSquare(size - 1) + [size*size]


# Test	Result
print(lstSquare(3))
# [1,4,9]
