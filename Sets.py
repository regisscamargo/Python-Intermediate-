myset = {1, 2, 3, 1, 2}
print(myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(3)
myset.clear(3)
myset.remove(3)

print(myset)


myset = {1, 2, 3, 1, 2}
print(myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print("yes")
    

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# i = odds.intersection(evens)
# print(i)

i = odds.intersection(primes)
print(i)

