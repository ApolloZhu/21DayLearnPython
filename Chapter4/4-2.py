numbers = [float(input("请输入一个数：")) for i in range(20)]
positive = [number for number in numbers if number > 0]
negative = [number for number in numbers if number < 0]
print(positive)
print(negative)
