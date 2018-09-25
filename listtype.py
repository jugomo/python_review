#import sys
#print(sys.version)


lst = [10, 20, 'HELLO', -20, 30.5]
print(lst)
print(lst[2])
print(lst[3:5])
print(lst*4)
print(len(lst))


lst.append(40)
print(lst)
lst.remove("HELLO")  # delete by value
print(lst)
del(lst[4])   # delete by index
print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse = True)
print(lst)

lst.clear()
print(lst)



