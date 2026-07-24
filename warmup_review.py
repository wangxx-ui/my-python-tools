#这一串代码是我再有几天没有学习和练习python后的第一天的复习，或许会有很多的bug希望大佬们见谅
name = input('请输入你的名字：')
age = input('请输入你的年龄：')
home = input('请输入你的家乡：')
print(f'我叫{name},我的年龄是{age},我的家乡是{home}')
score = int(input('请输入你的成绩：'))
if score>100:
    print('同学，你的成绩输错了哦')
if score<0:
    print('同学，你的成绩输错了哦')
elif score>=90:
    print('优秀')
elif score>=80:
    print('良好')
elif score>=60:
    print('及格')
#不能放在后面的原因是：这串注释的代码，放在后面，电脑会先执行前面的指令，会先输出优秀或者不及格
# elif score>100:
#     print('同学，你的成绩输错了哦')
# elif score<0:
#     print('同学，你的成绩输错了哦')
else:
    print('不及格')
num = 0
#range是算头不算尾
for i in range(1,101):
    num += i
print(num)
while  True:
    code = input('请输入密码：')
    if code =="123456":
        print('密码正确')
        break
    else:
        print('密码错误，请重试')
#后面已经说了，元组内部元素不能增删改，所以这个设置的变量就用处不大了
# student =()
students = list()
while True:
    name1 = input('请输入你的名字：')
    if name1=='quit':
        break
    score1 = input('请输入你的成绩：')
#这一步有两个错误点 ，1.这是一个已经创建的元组，元组是不能增删改内部的元素的；2.add()这个函数本身是不与元组使用的，这个是集合中用到的。
# student.add(name1,score1)
#在append()这个函数里面还加上括号，意味着把里面括号内的东西当作一个整体
    students.append((name1,score1))
print(len(students))
#虽然感觉不太值得写注释，但是，这个点是我经过一段时间才吃透的
#在这个for遍历中，i代表着students中的一个元组，i[1]或者i[0]则是代表在这些元组中的元素
for i in students:
    if i[1]>=60:

        print(i[0])
