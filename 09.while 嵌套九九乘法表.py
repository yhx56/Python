# print("Hello",end='')
# print("World",end='')

# 制表符
# print("Hello\tWorld")
# print("itheima\tbest")

# 九九乘法表
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j *i }\t",end='')
        j += 1

    i += 1
    print()
