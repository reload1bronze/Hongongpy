numbers = [3, 5, 9, 12]

print(max(numbers))


array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

array = [i * i for i in range(0, 20, 2)]
print(array)

output = [i for i in range(1, 100+1) if '{:b}'.format(i).count('0') == 1]

for i in output:
    print('{} : {}'.format(i, '{:b}'.format(i)))
print('합계:', sum(output))
