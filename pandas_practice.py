# 第一部分：Series 基础操作
#
# 创建与访问：
#
# 用 pd.Series 从列表 [10, 20, 30, 40] 创建一个 Series，索引设为 ['a','b','c','d']。
#
# 用标签索引打印 'b' 对应的值。
#
# 用位置索引打印第一个元素。
#
# 切片与统计：
#
# 创建一个包含 [1, 2, 3, 4, 5] 的 Series。
#
# 用位置切片取出前三个元素。
#
# 用 sum() 计算总和，并打印。
#
# 第二部分：DataFrame 基础操作
#
# 创建 DataFrame：
#
# 用字典 data = {'姓名':['张三','李四','王五'], '成绩':[85, 90, 78]} 创建一个 DataFrame df。
#
# 打印 df。
#
# 列操作：
#
# 给 df 添加一列 '班级'，值全部为 '一班'。
#
# 用 insert 方法在 '成绩' 列前面插入一列 '学号'，值为 [1, 2, 3]。
#
# 打印 df。
#
# 行与列访问：
#
# 用 iloc 打印第一行的数据。
#
# 用 loc 打印所有学生的姓名和成绩两列。
#
# 第三部分：数据筛选
#
# 条件筛选：
#
# 筛选出成绩大于等于80分的学生，并打印结果。


import pandas as pd

Ser = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

print(Ser)
#不加loc函数是也可以照常按照标签查找的
print(Ser['b'])

#但是，在不加上iloc时就是不能够直接写位置来查找值
print(Ser.iloc[0])

Ser1 = pd.Series([1,2,3,4,5])
print(Ser1.head(3))
print(Ser1.sum())

#加上个私心，其实也可以直接根据np.random.randint来创建一个随机数组
data = {'姓名':['张三','李四','王五'], '成绩':[85, 90, 78]}
data_odj = pd.DataFrame(data)
print(data_odj)

data_odj.insert(0,'班级','一班')

data_odj.insert(2,'学号',[1,2,3])

print(data_odj.iloc[0])

#这一个也可以写成print(data_odj.loc[...,['姓名','成绩']])
print(data_odj.loc[:,['姓名','成绩']])

print(data_odj[data_odj['成绩'] >= 80])

