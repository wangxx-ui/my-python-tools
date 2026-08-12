# 第一部分：NumPy 基础巩固
#
# 数组创建与运算：
#
# 用 np.arange() 创建一个从 1 到 10 的数组 arr1。
#
# 用 np.linspace() 创建一个从 0 到 1 的、包含 5 个等间距数字的数组 arr2。
#
# 将 arr1 的所有元素乘以 2，并将结果打印出来。
#
# 二维数组与形状：
#
# 创建一个包含数字 1 到 12 的列表，用 np.array() 把它变成二维数组 arr2d，形状为 3 行 4 列。
#
# 用 shape 属性打印它的形状。
#
# 用 reshape 方法把它的形状改成 4 行 3 列，并打印新数组。
#
# 第二部分：正则表达式复习
#
# 提取日期和金额：
#
# 给定字符串 text = "订单日期：2024-08-12，总金额：￥199.99元，优惠：-20.00元"
#
# 用 re.findall 和合适的正则表达式，提取出日期（年-月-日）。
#
# 用 re.findall 和合适的正则表达式，提取出所有的金额（包括小数点和负号，但不包括“￥”和“元”）。
#
# 第三部分：列表推导式与匿名函数复习
#
# 数据清洗与转换：
#
# 给定列表 prices = ['$19.99', '$25.00', '$8.50', '$100.00']。
#
# 用列表推导式，去掉每个元素前面的 $ 符号，并将其转换为浮点数，存入新列表 float_prices 并打印。
#
# 用 filter 和匿名函数，筛选出价格大于 20 的元素，并打印结果。
print('-'*30,'复习numpy简单应用')
import numpy as np
#啊，原来用arange创建数组，是创建区间数组啊，默认起始值是1
#从起始值开始，到终止值得前一个结束，也就是取不到终止值
arr1 = np.arange(1,11)
print(arr1)
#随机在起始值到终止值之间做等差数列，num默认50，但是现在改为5，也就是会生成只有5个数的一维数组
#默认可以取到终止值
arr2 = np.linspace(0,1,5)
print(arr2)
print(arr2*2)
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
#第一种比较简洁的方法
arr2d = np.array(list1).reshape(3,4)
#比较麻烦的是这种
#arr3 = np.array([1,2,3,4,],[5,6,7,8],[9,10,11,12])
print(arr2d.shape)
arr2d1 = np.reshape(arr2d,(4,3))
print(arr2d1.shape)


# arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr4 = np.array(range(1,13))
# #arr3=arr4
# #下面把arr3变成二维数组
# #括号里面一般是按照某行某列来算的
# arr5 = np.reshape(arr3,(3,4))
text = "订单日期：2024-08-12，总金额：￥199.99元，优惠：-20.00元"
import re
print(f'日期:{re.findall(r'\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])',text)}')
print(re.findall(r'-*\d+\.\d+',text))

print('-'*30,'下面是练习列表推导式')
prices = ['$19.99', '$25.00', '$8.50', '$100.00']
#price[1:]这个代表着从第二个字符串开始检索，后不封顶
float_prices  = [float(price[1:]) for price in prices ]
print(float_prices)
#这个匿名函数是结合上filter这个高级函数，filter自带遍历功能 语法是list(filter(匿名函数,想要让匿名函数检索的列表))
big_prices = list(filter(lambda price:price >20,float_prices))
print(big_prices)
