# 背景：你拿到了一份带有缺失值的销售数据，需要清洗数据、筛选出有效记录，并把结果保存到文件。
#
# 任务一：创建带缺失值的 NumPy 数组
#
# 导入 NumPy，创建一个一维数组 sales，包含以下数据：[120.5, np.nan, 89.9, np.nan, 200.0, 150.3]。
#
# 打印数组。
#
# 任务二：用布尔索引和 ~np.isnan() 清洗数据
#
# 用 ~np.isnan(sales) 筛选出所有非缺失值，存入 clean_sales。
#
# 打印 clean_sales。
#
# 任务三：定义装饰器（save_log）
#
# 定义一个装饰器 save_log，它能把函数的返回结果追加写入 result_log.txt 文件。
#
# 如果函数执行出错，打印“执行出错，结果未保存”，并返回 None。
#
# 提示：需要在装饰器内部用 try-except，并用 a 模式打开文件。
#
# 任务四：用装饰器保存清洗结果
#
# 用 @save_log 装饰一个函数 process_data(data)，它接收一个数组，计算平均值并返回一个格式化字符串，比如“有效数据共X条，平均销售额为Y元”。
#
# 调用 process_data(clean_sales)，并打印返回结果。
#
# 任务五：验证并查看日志
#
# 检查程序运行后，result_log.txt 文件是否正确记录了结果。
#
# 任务六：添加注释
# 为每个功能块添加清晰的注释。
import numpy as np
#先把一个列表转化为一维数组，方便后续处理
sales = np.array([120.5, np.nan, 89.9, np.nan, 200.0, 150.3])
print(sales)
#~就是取反的意思，原本np.isnan()这个函数是取空值的，但是加上取反就是获得纯数字数组
clean_sales = sales[~np.isnan(sales)]
print(clean_sales)

def save_log(func):
    def wrapper(*args, **kwargs):
        try:
            #下面注释掉的代码有一个明显的问题是，会调用两次函数
            # with open('result_log.txt', 'a', encoding='utf-8') as f:
            #     f.write(func(*args,**kwargs) + '\n')  <--写入文件
            # return func(*args,**kwargs)  <--调用函数，返回结果
            result = func(*args, **kwargs)
            with open('result_log.txt', 'a',encoding='utf-8') as f:
                f.write(result+'\n')
            return result
        except:
            print('执行出错，结果未保存')
            return None
    return wrapper
@save_log
def process_data(data):
    return f'有效数据共{len(data)}条，平均销售额为{np.mean(data)}元'
print(process_data(clean_sales))
