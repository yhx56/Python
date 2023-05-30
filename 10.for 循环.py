# name = "itheima"
# for x in name:
#     print(x)



# # 统计如下字符串中，有多少个字母a
# name = "itheima is a brand of itcast"
# # 定义一个变量，用来统计有多少a
# count = 0
# # for 循环统计
# # for 临时变量 in 被统计的数据：
# for x in name:
#     if x == "a":
#         count += 1
# print(f"被统计的字符串中有{count}个a")



# range 语法的使用
# 01
# for x in range(10):
#     print(x)

# 02
# for x in range(5,10):
#     print(x)
#

# 03
# for x in range(5,10,2):
#     print(x)
#

# for 循环临时变量的作用域
# i = 0
# for i in range(5):
#     print(i)
# print(i)



# for 嵌套循环

# for i in range(1,101):
#     print(f"今天是向小美表白的第{i}天，加油坚持")
#
#
#     for j in range(1,11):
#         print(f"给小美送的第{j}朵玫瑰花")
#
#     print("小美，我喜欢你")
#
# print(f"第{i}天，表白成功")



# for 九九乘法表
# for a in range(1,10):
#     for b in range(1,a + 1):
#         print(f"{b} * {a} = {b * a}\t",end='')
#     print()

money = 10000

for i in range(1,21):
    import random
    score = random.randint(1,10)

    if score < 5:
        print(f"员工{i}绩效分{score}，不满足，不发工资，下一位")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}，满足条件发放工资1000，公司账户余额：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，发不了，下个月再来")
        break













