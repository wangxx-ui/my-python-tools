# 背景：你要写一个用户管理系统，需要用到装饰器和异常处理来保证程序的健壮性。
#
# 已提供的数据（直接复制到你的代码里）：
#
# python
# users = {
#     'admin': {'password': '123456', 'role': '管理员'},
#     'user1': {'password': 'password', 'role': '普通用户'},
#     'guest': {'password': 'guest123', 'role': '游客'}
# }
# 任务一：定义装饰器（login_required）
#
# 定义一个装饰器 login_required，它检查用户是否已登录。
#
# 设置一个全局变量 current_user = None，代表当前登录的用户。
#
# 如果 current_user 为 None，打印“请先登录”，并返回 None。
#
# 如果已登录，则正常执行被装饰的函数。
#
# 任务二：定义登录函数（login）
#
# 定义一个函数 login(username, password)，验证用户名和密码。
#
# 如果登录成功，设置 current_user 为该用户名，并打印“登录成功，欢迎{用户名}”。
#
# 如果失败，用 raise 抛出 ValueError('用户名或密码错误')。
#
# 任务三：定义管理员专属功能（admin_only）
#
# 用 @login_required 装饰一个函数 view_all_users()，打印所有用户信息。
#
# 在这个函数内部，检查当前用户的角色是否为“管理员”。如果不是，用 raise 抛出 PermissionError('权限不足，仅管理员可查看')。
#
# 如果是管理员，遍历 users 字典，打印每个用户的用户名和角色。
#
# 任务四：测试整个流程
#
# 调用 view_all_users()，验证未登录时是否能正确拦截。
#
# 调用 login('admin', '123456')，登录管理员账号。
#
# 再次调用 view_all_users()，验证是否能正常查看。
#
# 调用 login('user1', 'password')，登录普通用户。
#
# 再次调用 view_all_users()，验证权限不足时是否能正确拦截。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释。
users = {
    'admin': {'password': '123456', 'role': '管理员'},
    'user1': {'password': 'password', 'role': '普通用户'},
    'guest': {'password': 'guest123', 'role': '游客'}
}
#先定义一个全局变量
current_user = None
def login_required(func):
    def wrapper(*args, **kwargs):
        # try:
        #     return func(*args, **kwargs)
        #检验登录
        if current_user is None:
            print('请先登录')
            return None
        else:
            return func(*args, **kwargs)
    return wrapper

def login(username, password):
    try:
        global current_user
        #一个我没想到的常识：
        #检验一个用户是否登陆成功应该看用户名跟密码是否能跟后台对的上
        if username in users and users[username]['password'] == password:
            current_user = username
            print(f'登录成功，欢迎{current_user}')
        else:
            raise ValueError
    except ValueError as e:
        print('用户名或密码错误')


@login_required
def view_all_users():
    try:
        #检查当前用户是否存在
        if current_user not in users:
            raise PermissionError('用户不存在')
        #检查当前用户是否为管理员
        #这个倒象是一次性的
        if users[current_user]['role'] != '管理员' :
            raise PermissionError('权限不足，仅管理员可查看')
        user_role = dict()
        for user in users.keys():
            user_role[user] = users[user]['role']
            print(user_role)
    except PermissionError as e:
        print(e)

#调试函数
view_all_users()
login('admin', '123456')
view_all_users()
login('user1', 'password')
view_all_users()
