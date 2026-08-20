# 背景：你拿到了一个在线商店的订单数据，需要完成多步骤的数据清洗、统计和筛选，并生成一份分析报告。
#
# 任务一：创建数据
# 用字典创建 orders DataFrame，包含以下列：
#
# 订单号：['A001','A002','A003','A004','A005','A006']
#
# 客户：['张三','李四','王五','张三','李四','赵六']
#
# 金额：[199.9, 89.0, 299.0, 49.9, 120.5, 399.0]
#
# 状态：['已完成','已取消','已完成','已完成','已取消','已完成']
#
# 任务二：数据清洗与转换
#
# 用 apply 给 金额 列打 9 折，结果保留两位小数，存入新列 折后金额。

# 用 apply 创建一个新列 金额等级，规则是：金额≥300为“大额”，≥100为“中额”，其他为“小额”。
#
# 任务三：分组聚合
#
# 按 客户 分组，用 agg 同时求每个客户的订单总数和平均金额。
#
# 按 状态 分组，统计每种状态的订单数量。
#
# 任务四：复杂筛选与排序
#
# 用 query 筛选出已完成且金额≥100的订单。
#
# 用 sort_values 按 折后金额 从高到低排序，并打印。
#
# 任务五：生成报告文件
#
# 把任务三中按客户分组的统计结果，写入 customer_report.txt 文件。
#
# 把任务四中筛选出的订单，追加写入同一个文件。
#
# 任务六：添加注释
# 为每个功能块添加清晰的注释。
import pandas as pd

df = pd.DataFrame({
    '订单号':['A001','A002','A003','A004','A005','A006'],
    '客户':['张三','李四','王五','张三','李四','赵六'],
    '金额':[199.9, 89.0, 299.0, 49.9, 120.5, 399.0],
    '状态':['已完成','已取消','已完成','已完成','已取消','已完成']
})

print(df)

#这一行的代码返回的是字符串，不符合要求
# df['折后金额'] = df['金额'].apply(lambda x:f'{x*0.9:.2f}')
#这个代码则是可以正常返回数字
df['折后金额'] = df['金额'].apply(lambda x: round(x * 0.9, 2))
#如果我记得没错的话，好像还能指定位置插入吧
# df.insert(3,'折后金额',df['金额'].apply(lambda x:f'{x*0.9:.2f}'))

print(df)

#三目运算符，添加新列，相融合
#我咋感觉这个等级不能按照金额来划定啊，应该用折后金额来划定吧
df['金额等级'] = df['金额'].apply(lambda x:'大额' if x >= 300 else '中额' if x >= 100 else '小额')
#跟上面一样，也同样可以用insert来插入

print(df)

#如果你要统计每个客户的订单数，应该用 'count' 或 'size
df.groupby('客户')['金额'].agg(['size','mean'])

print(df)

#groupby是一个方法，方法后面要跟上()
df.groupby('状态').agg('size')

df.query('状态=="已完成" and 金额>=100')

df_new = df.sort_values(by = '折后金额', ascending = False)

print(df_new)

with open('customer_report.txt','a',encoding='utf-8') as f:
    f.write(f'每个客户的订单总数和平均金额分别为：{df.groupby('客户')['金额'].agg(['size','mean'])}')
    f.write('\n')
    f.write(f'每种状态的订单数量分别为：{df.groupby('状态')['金额'].agg('size')}')
    f.write('\n')

with open('customer_report.txt','a',encoding='utf-8') as f:
    f.write(f'已完成且金额≥100的订单:{df.query('状态=="已完成" and 金额>=100')}')
    f.write('\n')

with open('customer_report.txt','r',encoding='utf-8') as f:
    print(f.read())

