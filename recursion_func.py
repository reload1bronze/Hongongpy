def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
        return output


def fact_recursion(n):
    if n == 0:
        return 1
    else:
        return n * fact_recursion(n-1)


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(35))
