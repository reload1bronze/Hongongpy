def bla():
    print('bla')


def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times('hello', 5)


def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()


print_n_times(3, '안녕하세요', 3, 3.4)


def print_n_times(value, n=2):
    for i in range(n):
        print(value)


print_n_times('안녕하세요')


def return_test():
    return


value = return_test()

print(value)


def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output


print(sum_all(start=0, end=10))


def function(a=10, b=20, *values):
    return a + b

print(function(3, 4, 9, 1))