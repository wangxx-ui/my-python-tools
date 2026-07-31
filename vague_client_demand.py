students_info = dict()
students_name = []
scores = []
print("请按照要求驶入学生的姓名跟对应的成绩，"
      "并且当学生姓名输入为 quit 时，"
      "系统会停止录入学生信息。")
while True:
    student_name = input('请输入学生名字：')
    if student_name == 'quit':
        break
    score = input('请输入学生的分数：')
    students_name.append(student_name)
    #因为后面要进行比较大小，所以要用到一个float函数
    scores.append(float(score))
    #这样写相对于直接写将键跟值直接添加到字典中
    #会更加的理解代码的逻辑
students_info = dict(zip(students_name, scores))
#学生人数可以直接用len函数直接求，不需要再用for遍历累加了，并且要注意的是不能直接用reduce函数求
#不然累加出来的会是一大串的学生姓名
students_num = len(students_name)
average = sum(scores) / students_num
not_good = []
#下面是把字典转化成了可以遍历的由元组组成的列表
#i就是列表中的元组
for i in students_info.items():
    #下面中的i[n]代表着元组内的对应序列的元素
    if i[1] <= 60:
        not_good.append(i[0])
        #下面就是简单的写入与追加了
with open('students_info.txt', 'w', encoding='utf-8') as f:
    f.write(f'总人数：{students_num}\n')
with open('students_info.txt', 'a', encoding='utf-8') as f:
    f.write(f'学生平均分：{average}\n')
    f.write(f'不及格同学名单：{not_good}')
