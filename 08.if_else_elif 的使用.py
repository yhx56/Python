# if的基本使用
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年，需要购买10元门票")
print("祝您玩的愉快！")

# if 加 else
age = int(input("请输入您的年龄:"))

if age >= 18:
    print("您已成年，需要买票10元")
else:
    print("您未成年，可以免费游玩。")

# 案例2
height = int(input("请输入您的身高（cm）："))

# 通过if 进行判断
if height > 120:
    print("您的身高超出120CM，需要购买10元门票。")
else:
    print("您的身高低于120CM，可以免费游玩。")
print("祝您玩的愉快。")


# if ，else ，elif
print("欢迎来到黑马动物园。")
height = int(input("请输入你的身高（CM）："))
vip_level = int(input("请输入您的VIP级别（1~5）："))
day = int(input("请输入今天的日期（1~30）："))
if height < 120:
    print("您的身高小于120CM，可以免费游玩。")
elif vip_level > 3:
    print("您的VIP级别大于3，可以免费游玩。")
elif day == 1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您玩的愉快。")

print("欢迎来到黑马动物园。")
if int(input("请输入你的身高（CM）：")) < 120:
    print("您的身高小于120CM，可以免费游玩。")
elif int(input("请输入您的VIP级别（1~5）：")) > 3:
    print("您的VIP级别大于3，可以免费游玩。")
elif int(input("请输入今天的日期（1~30）：")) == 1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您玩的愉快。")


# 小练习
# num = 5
#
# # 通过键盘输入获取猜想的数字，通过多次if 和 elif的组合进行猜想
# if int(input("请猜一个数字：")) == num:
#     print("恭喜你一次就猜对了。")
# elif int(input("猜错了，在猜一次：")) == num:
#     print("猜对了")
# elif int(input("猜错了，在猜一次。")) == num:
#     print("恭喜，最后一次机会，你猜对了。")
# else:
#     print("Sorry,猜错了")

# 嵌套
# if int(input("你身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果VIP级别大于3，可以免费")
#
#     if int(input("你的VIP等级是多少：")) > 3:
#         print("恭喜你，VIP级别达标，可以免费")
#     else:
#         print("Sorry,你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩。")


# 领取礼物
age = 20  # 年龄
year = 3  # 入职时间，年
level = 1 # 级别
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，丹斯入职实际和级别不达标。")

    else:
        print("不好意思，年龄太大")
else:
    print("不好意思，小朋友不可以领取")




