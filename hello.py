"""
    Hello World - Python
    Author: Julio Gonzalez
"""

print("hola mundo")


x = int(input("enter min: "))
y = int(input("enter max: "))
i = x

if i % 2 == 0: i = x+1
while i<=y:
    print(i)
    i+=2
    
    
print("end!")