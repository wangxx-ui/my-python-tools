# 背景：你需要写一个能自动重试读取文件内容的程序。如果文件不存在或读取失败，程序能自动重试，并把错误记录到一个日志文件里。
#
# 任务一：定义装饰器（retry_and_log）
#
# 定义一个装饰器 retry_and_log，它能让被装饰的函数在失败时自动重试3次。
#
# 如果函数执行成功，打印“操作成功”。
#
# 如果函数执行失败，打印“操作失败，正在重试第X次...”，并在每次失败时，把错误信息追加写入 error_log.txt 文件。
#
# 提示：需要用到 try-except、循环和文件写入。
#
# 任务二：定义文件读取函数（read_file）
#
# 用 @retry_and_log 装饰一个函数 read_file(filename)，它尝试用 with open 读取指定的文件。
#
# 如果文件存在，就返回文件的内容。
#
# 如果文件不存在，就用 raise 抛出一个 FileNotFoundError 异常。
#
# 任务三：测试装饰器
#
# 创建一个测试文件 test.txt，写入一些内容（比如你的名字和今天的日期）。
#
# 调用 read_file('test.txt')，验证装饰器能否正确处理正常情况。
#
# 调用 read_file('not_exist.txt')，验证装饰器能否捕获异常并自动重试，同时检查 error_log.txt 是否正确记录了错误信息。
#
# 任务四：批量读取多个文件（可选）
#
# 创建一个文件列表 file_list = ['test.txt', 'not_exist.txt', 'another.txt']。
#
# 用 for 循环遍历这个列表，对每个文件调用 read_file 函数。
#
# 用字典记录每个文件的读取状态（成功/失败），最后打印这个字典。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释，说明这段代码在做什么。
#能够重试三次的装饰器
def retry_and_log(fun,retries=3):
    #定义内部函数，跟inner一样
    def wrapper(*args, **kwargs):
        #重试装饰器都要有的for循环
        for i in range(retries):
            #装饰器中穿插异常处理
            try:
                result = fun(*args, **kwargs)
                print('操作成功')
                return result
            except Exception as e:
                print(f'操作失败，正在重试第{i+1}次')
                #在异常处理中添加文件写入的功能
                #还是有必要用a追加模式的，因为用写入的话
                #后面内容会覆盖掉前面的内容
                with open('error_log.txt','a',encoding='utf-8') as f:
                    f.write(f'操作失败，正在重试第{i+1}次')
        #跳出循环给出最终总结
        print('最终操作失败')
    #嵌套函数必备的返回内部函数
    return wrapper
#这个是小拓展
#@retry_and_log(retries=5)  # 重试 5 次
@retry_and_log
def read_file(file):
    #函数内部的异常处理
    try:
        #下面是可能出错的函数内容
        with open(file,'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        #抛出报错，异常冒泡
        #并对报错做出解释
        raise FileNotFoundError(f'文件{file}不存在')
    #为调试函数做出前提设置
with open('test.txt','w',encoding='utf-8') as f:
    f.write("""你好，这是一个测试文件。
今天是2026年8月10日。
我正在练习用装饰器处理文件操作。
天气很热，但学习不能停。
加油，你一定能掌握这些知识。""")
#这一个是在原本作业要求的基础上我抄的ai的能更简洁的方法
# # 2. 清空旧日志（可选，让每次运行从零开始）
# with open('error_log.txt', 'w', encoding='utf-8') as f:
#     f.write('')
print(read_file('test.txt'))
#输出结果太难看，做一个分隔符，还能稍微看得下去
print('-'*100)
print(read_file('not_exist.txt'))
print('-'*100)
with open('error_log.txt','r',encoding='utf-8') as f:
    print(f.read())
print('-'*100)
#这一个跟下面的打包组装是一个功能块的
# file_state = list()
file_dict = dict()
file_list = ['test.txt', 'not_exist.txt', 'another.txt']
for filename in file_list:
    result0 = read_file(filename)
    #给字典添加相应的键值
    file_dict[filename] = result0
    #用打包组装的方法会导致字典稍微杂乱
    # file_state.append(result0)
# file_dict = dict(zip(file_list,file_state))
print('-'*100)
print(file_dict)
