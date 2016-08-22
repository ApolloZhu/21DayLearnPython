import math

def square(num):
    return math.pow(num, 2)

def absolute(num):
    return math.fabs(num)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = float(input("Number: "))
    print(square(num))
    print(absolute(num))
    print(isPrime(num))
