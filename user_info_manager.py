#先收集用户的基本信息
name = input('请输入你的名字：')
age = int(float(input('请输入你的年龄：')))
ID_number = input('请输入你的身份证号：')
introduction = input('请输入你的个人简介（用一句话概述）：')
#然后看看用户填写的信息有没有原则性的错误
print(0<=age<=120,len(ID_number)==18,not(name==''),not(ID_number==''))
#根据用户的年龄来判断用户属于哪个年龄组，并为后面的输出年龄组做准备
if 0<=age<=6:
    age_group ='婴幼儿'
elif 7<=age<=17:
    age_group ='青少年'
elif 18<=age<=59:
    age_group = '成年人'
else:
    age_group = '老年人'
#开始进行if嵌套，先通过身份证号的第17位的奇偶来判断外层用户的性别，再通过年龄来进行内部if判断
x = int(ID_number[16:17])#也可以是 x = int(ID_number[16])
result =x%2#求余数的基本方法
if result==0:
    sex = '女性'
    if age<18:
        print('未成年女孩')
    else:
        print('成年女性公民')
else:
    sex = '男性'
    if age<18:
        print('未成年男孩')
    else:
        print('成年男性公民')
#最后，打印出名片
print(f'\t姓名：{name}\n\t年龄：{age}\n\t年龄段：{age_group}\n\t性别：{sex}\n\t个人简介：{introduction[0:8]}......')
