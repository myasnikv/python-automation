def main():
    print(list(generateFibonacci(22)))
    print(fib_second(13))
    print(singleFibNumber(9))


def generateFibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
        yield a


def fib_second(n):
    fibo = [0, 1]
    for i in range(n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def singleFibNumber(n):
    if type(n) != int or n < 0:
        return False
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return singleFibNumber(n-1) + singleFibNumber(n-2)

if __name__ == '__main__':
    main()
