lst= [1,2,3]

print(lst)
print(id(lst))

obj=lst
print(id(obj)==id(lst))

lst.pop()

print(lst)
print(id(lst))
print(obj)

print(id(obj)==id(lst))

lst.append(5)

print(obj)