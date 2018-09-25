# does not allow duplicates
# does not warrantee any order and not allow indexing
# does not allow repetition
from test.test_importlib import frozen

s = {10, 20, 30, "XYZ", 10, 20, 10}
print(s)
print(type(s))

s.update([88, 99])
print(s)

s.remove(30)
print(s)

#print(s[0])    # not indexable
#print(s[0:5])  # not subscriptable
#print(s*3)     # no allow repetition


# FROZEN SET

f = frozenset(s)
#f.update(20)
#f.remove(10)
