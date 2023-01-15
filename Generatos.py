#----------------------------------------------------------
# GENERATORS
#----------------------------------------------------------

def mygerenator():
    yield 1
    yield 2
    yield 3

g = mygerenator()

for i in g:
    print(i)

value = next(g)
print(value)

#----------------------------------------------------------
# countdown
#----------------------------------------------------------


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# you can iterate over a generator object with a for in loop
cd = countdown(3)
for x in cd:
    print(x)     

# this will raise a StopIteration
print(next(cd))

cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)
     
#----------------------------------------------------------
# Big advantage: Generators save memory!
#----------------------------------------------------------

def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")


# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")


def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))

#----------------------------------------------------------
# Generator expressions
#----------------------------------------------------------

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))
     

class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()
             
firstn_object = firstn(1000000)
print(sum(firstn_object))