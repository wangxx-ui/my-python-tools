#1.编写一个循环，循环3次 2.要从1-10之间选择一个随机数 3.if分支判断
import random
#第一步 定义一个变数器
i=1
#第四步 生成1-10的随机数
suijishu=random.randint(1,10)
#第二步 编写循环体
while i<=3:
    #第五步 提示用户输入数字
    usernum=int(input('请输入你猜的数字（范围在1-10之间）：'))
    #第六步 判断用户输入的数字是否与随机数相等
    if usernum==suijishu:
        print('恭喜你猜对了！！！！')
        break
    elif usernum<suijishu:
        print('猜小了哦')
    else:
        print('猜大了哦')
#更新变数器
    i+=1
