# Use list comprehension approach to write a function lstSquare(n:Int) that returns a list of the squares of the numbers from 1 to n?

def lstSquare(n):
    # range(n) có nghĩa là 0 tới n-1
    # range(1,n) có nghĩa là 1 tới n-1
    # vậy giờ muốn tạo từ 1 tới n thì viết range ntn? range(1,n+1)

    # vậy giờ viết theo kiểu thông thường, dài dòng là như lào
    newlist = []
    for i in range(1, n+1):
        newlist.append(i**2)

    # đây là cách viết list comprehension, tức ngắn gọn, làm biếng đồ á
    return [i ** 2 for i in range(1, n+1)]
    


print(lstSquare(3))
# [1,4,9]
