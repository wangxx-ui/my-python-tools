# 背景：你拿到了一个学生的成绩表，需要用三目运算符和列表推导式完成数据转换和筛选。
#
# 任务一：创建 DataFrame
# 用字典创建 df，包含两列：
#
# '姓名'：['张三','李四','王五','赵六','孙七']
#
# '成绩'：[58, 76, 89, 45, 92]
#
# 任务二：用列表推导式创建新列
#
# 用列表推导式生成一个新列表 level_list，规则：成绩≥85为“优秀”，≥60为“及格”，其他为“不及格”。
#
# 把 level_list 添加到 df 中，列名为 '等级'，打印 df。
#
# 任务三：用三目运算符计算加分
#
# 用 apply 和三元运算符给成绩加5分，但超过100分就按100分算。
#
# 把结果存入新列 '加分后成绩'，打印 df。
#
# 任务四：用列表推导式筛选数据
#
# 用列表推导式筛选出所有加分后成绩大于等于60分的学生姓名，存入列表 passed，并打印。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释。
import pandas as pd
import numpy as np

df = pd.DataFrame({
    '姓名':['张三','李四','王五','赵六','孙七'],
    #在这一行，我没有按照作业要求写，我自己多运用了个知识
    '成绩':np.random.randint(50,100,5)
})

print(df['成绩'])

#由这个烂的一坨的代码可以看出来，我的列表推导式，真的很差
#我是真没想到，我举例成功只多一个逗号啊
# level_list = ['优秀'if  100>= x >=85 else '及格' if x>=60 else '不及格', for x in df['成绩'] ]

level_list = ['优秀'if  100>= x >=85 else '及格' if x>=60 else '不及格' for x in df['成绩'] ]
df['等级'] = level_list
print(df)

#在这一行代码中，我用到了我很少用到过的  !=   这个符号，我记得是不等于
# df['成绩'].apply(lambda x: x+5 if x+5 !=100 else x+5)
#这一串代码是无效代码（我觉得无效是因为没有完成我的要求）
df['成绩'].apply(lambda x: x+5 if x+5 !=100 else 100)

# df['成绩'].apply(lambda x: x+5 if x+5 !=100 else 100)
# 跟这串代码相同意思的有
# 1.只是把对应值的顺序变了
# df['加分后成绩'] = df['成绩'].apply(lambda x: 100 if x + 5 > 100 else x + 5)
# 2.用到了min函数，用 min 是最安全的，它会自动取两者中较小的那个，超过100就取100
# df['加分后成绩'] = df['成绩'].apply(lambda x: min(x + 5, 100))

df['加分后成绩'] = df['成绩'].apply(lambda x: x+5 if x+5 !=100 else 100)
print(df)

df.query('加分后成绩>=60')['姓名']

passed = list()

#这个写法输出的结果不美观
#列表自带的功能
passed.append(df.query('加分后成绩>=60')['姓名'])
print(passed)

passed1 = list()

#列表推导式
passed1 = [x for x in df.query('加分后成绩>=60')['姓名']]

print(passed1)
