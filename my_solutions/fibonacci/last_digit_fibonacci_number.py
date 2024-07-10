def last_digit_fibonacci_number(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append((f[i-1] + f[i-2])%10)
    return f[n]

if __name__ == '__main__':
    while True:
        input_n = int(input())
        print(last_digit_fibonacci_number(input_n))
