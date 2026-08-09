# 定义重试装饰器：当被装饰函数失败时，自动重试最多3次
def retry_on_failure(fun):
    #定义装饰器里面的内部函数
    def wrapper(*args, **kwargs):
        #增加功能
        for i in range(3):
            #异常处理
            try:
                #可能出错的函数内容
                result = fun(*args, **kwargs)
                print('执行成功')
                return result
            except:
                #出错后会返回的内容
                #因为在循环内部，所以会返回3次该形式的语句
                #循环里面的结果
                print(f'执行失败，正在重试第{i+1}次')
        #在循环之外，做一个总结
        #循环之外的结果
        print('重复执行了三次，执行失败')
    # 装饰器必须返回内部函数，用来替换原函数
    return wrapper
users = {'admin': '123456', 'user1': 'password', 'guest': 'guest123'}
#调用装饰器
@retry_on_failure
#定义被装饰的原函数
def query_user(username):
    #函数内部嵌套if条件语句
    if username in users.keys():
        #为啥不能直接输出
        #因为在装饰器里面还要调用这个内容
        return  f'用户的密码为：{users[username]}'
    else:
        #raise是相当于提前为报错做准备
        #('该用户不存在') 则是进一步解释报错
        raise ValueError('该用户不存在')
query_user('admin')
query_user('not_exist')
def query_user1(username):
    #举一反三，用字典中常用的get函数可以简化代码
    return users.get(username, '用户不存在')
print(query_user1('admin'))
print(query_user1('not_exist'))
