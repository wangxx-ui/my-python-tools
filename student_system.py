 keys =['name', 'age', 'score']#创建一个 键 的列表
name1 = input('请输入你的姓名：')#创建一个 值 的列表
age1 = int(input('请输入你的年龄：'))#同上
score1 = int(input('请输入你的成绩：'))#同上
student = dict(zip(keys, [name1, age1, score1]))#把四个列表先打包再根据规则分别归属到各自的键上
print(student)
students =list()
count=0
while True:#这是创建一个死循环，有break
    name2 = input('请输入你的姓名：')
    if name2 == 'quit':
        break#一定要先停止名字输入后再记数
    count += 1
    age2 = int(input('请输入你的年龄：'))
    score2 = int(input('请输入你的成绩：'))
    students.append((name2, age2, score2))#这个append把元素（以元组的形式）放到列表后面
print(students)
courses = ('Python', 'Java', 'C++')
print(courses)
count_60=0
count_80=0#规定计数器
for i in students:#现在i就是整个元组（这个元组指的是一个学生的一套信息）
    if i[2]>=60:#i[2]才是成绩
        count_60+=1
    if i[2]>=80:
        count_80+=1#把计数器根据设定叠加数值
print(count_60,count_80)
students.sort(key=lambda x: x[2], reverse=True)#把列表变成降序,因为列表是由好多个元组组成的，所以要想按照成绩排序就需要对成绩所在的位置索引（应该是这个意思）
print(students)
name3 = input('请输入你的姓名：')
#因为名字是在列表中的元组中的，所以就会比较很麻烦
found = False#先假设found是不成立
for stu in students:#同理这个stu也是元组
    if stu[0]==name3:#如果列表中的没一个元组中的第一的元素就等于 name3
        found = True#那么就会得出found是真的，也就是推翻了之前的假设
        break#并且破坏这个循环
if found:#重新列一个条件语句判断   如果found = True
    print(name3)
else:
    print('该学生不在列表中')
max_score = max(students, key=lambda x: x[2])
min_score = min(students, key=lambda x: x[2])
print(f'\t学生总人数:{count}\n\t及格人数:{count_60}\n\t优秀（≥80）人数:{count_80}\n\t最高分:{max_score[2]}\n\t最低分:{min_score[2]}\n\t排序后的学生列表:{students}')
