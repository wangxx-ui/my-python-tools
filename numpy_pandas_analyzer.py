# 背景：你拿到了一个班级的考试成绩数据，需要用 NumPy 和 Pandas 完成数据整理、统计和筛选。
#
# 任务一：用 NumPy 生成随机成绩
#
# 用 np.random.randint(50, 100, size=10) 生成10个50到100之间的随机整数，作为10名学生的成绩。
#
# 用 np.mean 计算平均分，并用 f-string 打印（保留1位小数）。
#
# 任务二：用 Pandas 创建 DataFrame
#
# 创建一个字典，包含两列：
#
# '姓名'：['张三','李四','王五','赵六','孙七','周八','吴九','郑十','钱十一','陈十二']
#
# '成绩'：任务一中生成的成绩数组
#
# 用 pd.DataFrame 创建 DataFrame，并打印。
#
# 任务三：添加列与筛选
#
# 给 DataFrame 添加一列 '评级'，规则是：成绩≥85为“优秀”，≥70为“良好”，≥60为“及格”，其他为“不及格”。
#
# 提示：可以用列表推导式或循环来完成。
#
# 筛选出评级为“优秀”的学生，并打印结果。
#
# 任务四：统计分析
#
# 用 Pandas 的方法计算成绩的最高分、最低分和标准差。
#
# 用 f-string 格式化输出这三项统计结果。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释。
import numpy as np


#给10个学生随机生成成绩
#前面可取，后面不可取
data0 = np.random.randint(50,100,size=10)
print(data0)

average_data0 = np.mean(data0)
print(f'10个学生的平均成绩是：{average_data0:.1f}')

import pandas as pd

data_dict = {'姓名':['张三','李四','王五','赵六','孙七','周八','吴九','郑十','钱十一','陈十二'],'成绩':data0}
data_df = pd.DataFrame(data_dict)
print(data_df)

#先创建列表
#这个是运用了三目运算符
#列表推导式 不能有两个中括号嵌套
rank = [ '优秀' if score >= 85 else '良好' if score >= 70 else '及格' if score >= 60 else '不及格' for score in data_df['成绩']]

#加上评级
data_df['评级'] = rank
print(data_df)

#下面这行代码是两层逻辑
#里面那层是先找评级在优秀的标签，然后根据这个优秀的标签来找数据
good_student = data_df[data_df['评级']=='优秀']
print('优秀学生')
print(good_student)

#牢记：这些函数，括号里面不能有任何东西
#numeric_only=True 的意思是："只对数值类型的列（int、float）进行计算，忽略文本列（string
data_max =data_df.max(numeric_only=True)   # 每列最大值
data_min = data_df.min(numeric_only=True)   # 每列最小值
#下面这个是求标准差
#求所有数值的标准差
data_std = data_df.std(numeric_only=True)
#求单列的标准差
data_std0 = data_df['成绩'].std()

print(f'\t最大值：{data_max}\n\t最小值：{data_min}\n\t标准差：{data_std0}')
