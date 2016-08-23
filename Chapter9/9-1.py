from math import sqrt
class PrimeIterator():
    def __init__(self, end):
        self.__current = 1
        self.__end = end

    def isPrime(self):
        num = self.__current
        if num <= 1:
            return False
        elif num != 2:
            if num % 2 == 0:
                return False
            for i in range(3, int(sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        while self.__current < self.__end:
            self.__current += 1
            if self.isPrime():
                return self.__current
        raise StopIteration

if __name__ == "__main__":
    print(list(PrimeIterator(int(input("One more than end: ")))))
