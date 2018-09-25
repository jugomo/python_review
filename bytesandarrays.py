# BYTES
# does not allow indexing and assign

# BYTEARRAY
# allows indexing and modify


lst = [20,3,40,234]
print(type(lst))


b = bytes(lst)
print(type(b))
#b[2] = 54

ba = bytearray(lst)
print(type(ba))
ba[2] = 33
