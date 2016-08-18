numbers = []
for i in range(10):
    numbers.append(float(input("请输入学生分数：")))
total = sum(numbers)
print("总分:",total)
print("平均分:",total/len(numbers))
