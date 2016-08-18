numbers = []
for i in range(5):
    numbers.append(int(input("请输入一个整数：")))
print(numbers[1::2])
print(numbers[-2::-2][::-1])
