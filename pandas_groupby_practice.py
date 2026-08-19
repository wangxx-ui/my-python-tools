# 背景：你拿到了一个公司的员工信息表，需要按部门统计薪资，并处理一些列数据。
#
# 任务一：创建 DataFrame
#
# 用字典创建 df，包含三列：
#
# '姓名'：['张三','李四','王五','赵六','孙七','周八']
#
# '部门'：['技术部','销售部','技术部','销售部','技术部','人事部']
#
# '薪资'：[12000, 8000, 15000, 9000, 11000, 7000]
#
# 打印 df。
#
# 任务二：用 groupby 和 agg 统计
#
# 按 '部门' 分组，用 agg 同时求每个部门的平均薪资和最高薪资。
#
# 打印统计结果。
#
# 任务三：用 apply 处理数据
#
# 给 df 添加一列 '薪资等级'，规则是：薪资≥12000为“高”，≥8000为“中”，其他为“低”。
#
# 提示：用 apply 和匿名函数。
#
# 打印 df。
#
# 任务四：排序与筛选
#
# 用 sort_values 按薪资从高到低排序，并打印。
#
# 用 query 筛选出薪资大于10000的员工，并打印。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释。
import pandas as pd

df = pd.DataFrame({
    '姓名':['张三','李四','王五','赵六','孙七','周八'],
    '部门':['技术部','销售部','技术部','销售部','技术部','人事部'],
    '薪资':[12000, 8000, 15000, 9000, 11000, 7000]
})

print(df)

#df.groupby('部门') 这个部分是分组，加上['薪资']就变成了把分好的组中对应的这一列取出来
result = df.groupby('部门')['薪资'].agg(['mean', 'max'])
print(result)

#经过这一串代码，我深刻意识到了我的三目运算符是有多么的差劲
df['薪资等级'] = df['薪资'].apply(lambda x: '高' if x >= 12000 else'中' if x>=8000 else'低')

#这行注释是我抄的ai的
# df['薪资等级'] = df['薪资'].apply(lambda x: '高' if x >= 12000 else '中' if x >= 8000 else '低')

print(df)

# .sort_values的相关参数
# by：指定按哪一列排序。比如 df.sort_values('薪资')。
#
# ascending：控制升序还是降序。默认是 True（升序），要降序就写 ascending=False。
#
# inplace：是否直接修改原 DataFrame。默认是 False，会返回一个新排序好的 DataFrame。

df.sort_values(by='薪资',ascending=False)
print(df.sort_values(by='薪资',ascending=False))
good_salary = df.query('薪资>10000')

print(good_salary)
