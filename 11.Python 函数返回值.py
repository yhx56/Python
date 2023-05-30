# # def add(a,b):
# #     result = a + b
# #     return result
# # r = add(5,6)
# # print(r)
#
#
#
# # 无return语句的函数返回值
# def say_hi():
#     print("你好呀")
# result = say_hi()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
# # 主动返回None的函数
# def say_hi2():
#     print("你好呀")
#     return None
#
# result = say_hi2()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
#
# # None 用于if判断
# def check_age(age):
#     if age > 18:
#         return "SUCCESS"
#     else:
#         return None
#
# result = check_age(14)
# if not result:
#     print("未成年，不可以进入")
#
#
#
#  定义函数，进行文档说明
# def add(x,y):
#     """
#     add 函数可以接收2个参数，进行相加
#     :param x: x表示其中一个数字
#     :param y: y表示其中一个数字
#     :return: 2个数字相加的结果
#     """
#     result =  x + y
#     print(f"2数相加的结果是：{result}")
#     return result
# add(1,1)
#
#
#
# 函数嵌套调用
# def func_b():
#     print("---2---")
#
# def func_a():
#     print("---1---")
#
#     func_b()
#
#     print("---3---")
# func_a()




"""
演示在函数使用的时候，定义的变量作用域
"""

# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()
# 出了函数体，局部变量就无法使用了
# print(num)

# 演示全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
#
# def test_b():
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
#
# def test_b():
#     num = 500       # 局部变量
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# global关键字，在函数内声明变量为全局变量
num = 200

def test_a():
    print(f"test_a: {num}")

def test_b():
    global num      # 设置内部定义的变量为全局变量
    num = 500
    print(f"test_b: {num}")

test_a()
test_b()
print(num)




