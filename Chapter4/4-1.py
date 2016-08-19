s1 = int(input("第一门子课程得分："))
s2 = int(input("第二门子课程得分："))
if s1 < 60:
    print("不及格")
elif s2 < 60:
    print("补考")
else:
    print("通过")
