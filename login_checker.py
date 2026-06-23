#第一步 预设正确的用户名和密码
user_name='user123'
user_code='pwd123'
#第二步 输入用户名和密码
user_name1=input('请输入你的用户名：')
user_code1=input('请输入你的密码：')
#第三步 进行if else的判断
if user_name1==user_name and user_code1==user_code:
    print('登陆成功')
else:
    print('用户名或密码错误，请重新输入')
