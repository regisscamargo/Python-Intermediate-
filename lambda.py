#lambda

add10 = lambda x:x + 10
print(add10)

def add10_func(x):
    return x + 10


mult = lambda x, y: x*y
print(mult(2,7))

points2d = [(1,2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key = lambda x: x[1])

print(points2d)
print(points2d_sorted)

def sort_by_y(x):
    return x[1]

points2d = [(1,2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key = sort_by_y)

a = [1, 2, 3, 4]
c = [x*2 for x in a]
print(c)

c = [x for x in a if x%2==0]
print(c)

#reduce

from functools import reduce

a = [1, 2, 3, 4, 5]
product_a = reduce(lambda x, y: x*y, a )
print(product_a)

