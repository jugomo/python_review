s1 = "   hello world   x  "

s2 = """
string in
multiple 
lines
"""



print(s1)
print(s2[3])
print(s1*2)
print(s2[2:5])

print(s1.strip())   #remove spaces
print(s1.lstrip())
print(s1.rstrip())

print(s2.find("in"))
print(len(s2))
print(s2.replace("mul", "caca"))
print(s2.upper())
print(s2.lower())
