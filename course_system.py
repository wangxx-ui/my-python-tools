student = {}#也可以使用dict()函数来创建这个空字典
name=[]
id0=[]#这是两个空列表
name1 = input('请输入你的名字：')
id1 = input('请输入你的学号：')
name.append(name1)#独属于列表的添加功能
id0.append(id1)
student = dict(zip(name, id0))#在这里会出现一个黄色警报，意思大概是上面的那个空字典你没用上
print(student)
courses = set()#只有这一种的空集合的创建方式
while True:
    courses1 = input('请输入你所选的课程：')
    if courses1=='quit':
        break
    courses.add(courses1)#集合中的元素添加方式
print(courses)
key = input('请输入一个新建：')
value = input('请输入一个新值：')
student[key] = value#因为这个key并不在字典中，所以相当于是在字典中添加了一个键和对应的值
key2 = input('请输入一个新建：')
if key2 in student:
    del student[key2]#这个删除不仅是删除key2这个键，还删除了对应的值
else:
    print('该键不存在')
print(student)
required_courses = {'Python', '数学', '英语'}
print('学生已选的必修课',required_courses & courses)#交集
print('学生还未选的必修课',required_courses - courses)#差集，前面集合包含的元素且后面集合不包含的元素
print(f'\t学生姓名:{name}\n\t学号:{id0}\n\t已选课程总数:{len(required_courses & courses)}\n\t已选必修课:{required_courses & courses}\n\t未选必修课：{required_courses - courses}')
