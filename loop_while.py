import time

a = range(10)

print(a)

b = list(a)

print(b)

for i in range(5):
    print(i)

print()

for i in list(range(5)):
    print(i)


array = [244, 234, 32, 345, 65]

for i in range(len(array)):
    print(f'{i} 번째는 {array[i]}')

for i in range(4, 0 - 1, -1):
    print(i)

for i in reversed(range(5)):
    print(i)

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print(number)
