# if、else 判断数字大小

import random
num = random.randint(1,10)

guess_num = int(input("输入你要猜测的数字："))
if guess_num == num:
    print("恭喜你，第一次就猜对了。")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了。")

    guess_num = int(input("输入你要再次猜测的数字："))

    if guess_num == num:
        print("恭喜你，第二次猜中了。")
    else:
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")

        guess_num = int(input("输入你要第三次猜测的数字："))

        if guess_num == num:
            print("第三次猜对了")
        else:
            print("三次机会用完了，没有猜中。")



