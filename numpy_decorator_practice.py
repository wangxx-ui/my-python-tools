# 背景：你要写一个数据分析小工具，需要用到装饰器来记录函数的执行时间，并用NumPy处理数据。
#
# 任务一：定义装饰器（log_execution）
#
# 定义一个装饰器 log_execution，它能在函数执行前打印“开始执行函数...”，执行后打印“函数执行完毕”。
#
# 如果函数执行出错，用 try-except 捕获异常，打印“函数执行出错”，并返回 None。
#
# 任务二：用NumPy处理数据
#
# 用 np.arange 创建一个从1到20的数组，并用 reshape 把它变成4行5列的二维数组 arr。
#
# 用 np.mean 计算 arr 的平均值，并用 f-string 打印出来（保留2位小数）。
#
# 任务三：用列表推导式筛选数据
#
# 给定列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]。
#
# 用列表推导式，筛选出所有偶数，并打印结果。
#
# 任务四：综合应用装饰器
#
# 用 @log_execution 装饰一个函数 analyze_data()，它内部调用任务二和任务三的功能，并打印“数据分析完成”。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释。

def log_execution(func):
    def wrapper(*args, **kwargs):
        try:
            print(f'开始执行函数{func}')
            func(*args, **kwargs)
            print('函数执行完毕')
        except Exception as e:
            print('函数执行出错')
            return None
    return wrapper
print('numpy简单函数练习','-'*30)
import numpy as np
#初始值可取，终止值不可取
# arange跟array在创建数组时，前者是区间 ，后者即可以直接把列表（数组序列）转化为数组，也可以结合range函数做区间数组
arr1 = np.arange(1,21)
arr = np.reshape(arr1,(4,5))
#求平均值  下面的这两个方法是等价的
#1.
print(arr.mean())
#2.
print(np.mean(arr))

#还需要把这个平均值给转化为2位小数
print(f'arr这个数组的平均值：{np.mean(arr):.2f}')
print('列表推导式','-'*30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = [i for i in numbers if i%2==0]
print(num)

print('应用装饰器','-'*30)
@log_execution
def analyze_data(numbers0):
    arr0 = np.array(numbers0)
    #用下面这个函数求平均值默认是跟mean结果一样，但是下面这个函数还能够求加权平均值
    #说实话，我也不知道怎样才能让这个函数求加权平均数
    #所以，我只是在这里提一嘴
    average = np.average(arr0)
    print(f'数组平均数为：{average:.2f}')
    num0 = [i for i in numbers0 if i%2==0]
    print(f'偶数列表：{num0}')
    print('数据分析完成')

#调试结果
analyze_data([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
