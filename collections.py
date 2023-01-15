#collectioms: counter, namedtuple, OrderedDict, defaultdict, dque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


a = "aaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter)

a = "aaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter.most_common(1))

a = "aaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter.most_common(1)[0][0])

a = "aaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter.elements())

point = namedtuple('Point', 'x, y')
pt = point(1, -4)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['a'] = 3
ordered_dict['a'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

d = defaultdict(int)
d['a'] = 1
d['a'] = 2
print(d['c'])

d = deque()

#----------------------------------------------------------
# POP, APPEND, DICT, EXTEND, ROTATE
#----------------------------------------------------------

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([3, 4, 5])
print(d)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)