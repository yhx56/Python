# 通过展位形式，完成拼接
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num,avg_salary)
print(message)


# %s转换成字符串
# %d转换成整数
# %f转换成浮点数
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s,成立于：%d，我今天的股价是：%f" % (name,setup_year,stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制，小数精度2，结果是：%2f" % num2)


name = "传智播客"
set_up_year = 2006
stock_price = 19.99
# f: format
print(f"我是{name}，我成立于：{set_up_year}年，我今天的股价是：{stock_price}")


# 对表达式进行格式化
print("1*1 的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))







