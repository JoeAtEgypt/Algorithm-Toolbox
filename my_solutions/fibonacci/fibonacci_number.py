def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fast_fibonacci_number(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

def one_operation_fibonacci_number(n):
    return int(1/(5**(1/2)) * ((((1 + (5**(1/2))) / 2) ** n) - (((1 - (5**(1/2))) / 2) ** n)) )

import random

if __name__ == '__main__':
    while True:
        # input_n = int(input())
        input_n = random.randint(1, 80)
        print(input_n)
        print(f"{fast_fibonacci_number(input_n)}  {one_operation_fibonacci_number(input_n)}")
        assert fast_fibonacci_number(input_n) == one_operation_fibonacci_number(input_n)
