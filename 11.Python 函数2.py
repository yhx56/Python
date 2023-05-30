# 定义2数相加的函数，通过参数接收被计算的两个数字
# def add(x,y):
#     result = x + y
#     print(f"{x} + {y}的计算结果是：{result}")
#
# # 调用函数
# add(1,8)


# def add(x,y,z):
#     result = x + y + z
#     print(f"{x} + {y} + {z}的计算结果是：{result}")
#
# # 调用函数
# add(1,8,1)



# 练习
def check(num):
    print("欢迎来到我司面试，请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if num <= 37.5:
        print(f"体温测量中，您的体温是：{num}度，体温正常请近")
    else:
        print(f"体温测量中，您的体温是：{num}度，需要隔离！")
check(37.5)






















