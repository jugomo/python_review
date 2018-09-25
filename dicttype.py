dict1 = {1:"julio", 2:"glez", 3:"mr"}
print(type(dict1))

print(dict1)
print(dict1.items())
print(dict1.keys())

k = dict1.keys()
for i in k:
    print(i)
    
print("\n")
    
v = dict1.values()
for i in v:
    print(i)

del dict1[2]
print(dict1)