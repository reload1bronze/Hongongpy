a = [1, 2, 3]
b = list(a)

b[1] = 3

print(a)
print(b)

print('문자열'[0])

a.insert(1, 7)
print(a)

list_a = [1, 2, 3]
list_a.extend([5])
print(list_a)

list_c = [0, 1, 2, 3, 4, 5]
del list_c[0]

list_c.pop(-1)
print(list_c)
