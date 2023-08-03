# Use high-order function approach to write function lstSquare(n:Int) to return a list of i square for i from 1 to n?

# high-order function gồm 3 hàm: map,filter,reduce
# map:
# filter:
# reduce:

# map và filter được sử dụng trong bài toán ko có tính liên kết giữa các phần tử

def lstSquare(n):
    return list(map(lambda x: x ** 2, range(1, n+1)))


print(lstSquare(3))
# [1,4,9]
