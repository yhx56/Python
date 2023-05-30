# 定义一个列表 list
my_list = ["itheima","itast","python"]
print(my_list)
print(type(my_list))

my_list = ["ktheima",666,True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [ [1,2,3,],[4,5,6] ]
print(my_list)
print(type(my_list))


# 通过下标索引取出对应位置的数据
my_list = ["Tom","Lily","Rose"]
# 列表[下标索引]，从前向后从0开始，每次+1，从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 通过下标索引引取数据（倒序取出）
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 取出嵌套列表元素
my_list = [ [1,2,3],[4,5,6] ]
print(my_list[1][2])



