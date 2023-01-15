from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat

a = [1, 2]
b = [3, 4]

prod = product(a,b)
print(list(prod))


a = [1, 2]
b = [3, 4]

prod = product(a,b, repeat=2)
print(list(prod))

a = [1, 2]
b = [3]

prod = product(a,b, repeat=2)
print(list(prod))

a = [1, 2, 3]

perm = permutations(a)
print(list(perm))

perm = permutations(a, 2)
print(list(perm))

a = [1, 2 , 3, 4]
comb = combinations(a, 2)
print(list(comb))

a = [1, 2 , 3, 4]
comb = combinations(a, 2)
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

a = [1, 2 , 3, 4]
comb = combinations(a, 2)
acc = accumulate(a, func=max)
print(a)
print(list(acc))

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

    a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

for i in count(10):
    print(i)

    if i == 15:
        break

