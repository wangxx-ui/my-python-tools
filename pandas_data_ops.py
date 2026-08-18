# 背景：你拿到了两个班级的成绩数据，需要完成数据整理、计算和统计。
#
# 任务一：创建 DataFrame
#
# 用字典创建 df1，包含列：'姓名' 为 ['张三','李四','王五']，'成绩' 为 [85, 90, 78]。
#
# 用字典创建 df2，包含列：'姓名' 为 ['赵六','孙七']，'成绩' 为 [88, 76]。
#
# 用 concat 将 df1 和 df2 纵向拼接成 df_all，并打印。
#
# 任务二：统计与计算
#
# 用 Pandas 计算 df_all 成绩列的平均分、最高分、最低分，分别打印。
#
# 用 f-string 格式化输出这三项结果。
#
# 任务三：排序与索引
#
# 用 sort_values 按成绩从高到低排序，并打印。
#
# 用 set_index 把 '姓名' 设为索引，并打印。
#
# 任务四：字符串处理
#
# 给 df_all 添加一列 '备注'，值为 [' good ', ' excellent ', ' pass ', ' good ', ' fail ']。
#
# 用 .str.strip() 去掉 '备注' 列首尾的空格，并打印处理后的 DataFrame。
#
# 任务五：筛选
#
# 用 query 筛选出成绩大于等于80分的学生，并打印。
#
# 任务六：添加注释
# 为每个功能块添加清晰的注释。
import pandas as pd

df1 = pd.DataFrame({'姓名':['张三','李四','王五'],'成绩':[85, 90, 78]})
print(df1)

df2 = pd.DataFrame({'姓名':['赵六','孙七'],'成绩':[88, 76]})
print(df2)

df_all = pd.concat([df1,df2])
print(df_all)

#inplace=True的含义就是在本质上面df_all已经被改变了
df_all.set_index(keys='姓名',inplace=True)

print(df_all)

#要么是在括号里面写上numeric_only=True
# average = df_all.mean(numeric_only=True)
average_score = df_all['成绩'].mean()
print(average_score)

max_score = df_all['成绩'].max(numeric_only=True)

min_score = df_all['成绩'].min(numeric_only=True)

print(f'\t平均成绩：{average_score}\n\t最高成绩:{max_score}\n\t最低成绩:{min_score}')

#这个就是按照成绩这一列且降序来排列
df_all.sort_values('成绩',ascending=False)

df_all['备注']=[' good ', ' excellent ', ' pass ', ' good ', ' fail ']

print(df_all)

#这个方法是创建一个新对象
df_all_new = df_all['备注'].str.strip()

#打印出备注这一列的内容
print(df_all['备注'].str.strip())
#打印出对象全部的内容
print(df_all_new)
#下面这一行是会返回全部都是true，因为现在调用的还是原来的对象
df_all['备注'].str.contains(' ')

df_new = df_all.query('成绩>80')

print(df_new)
