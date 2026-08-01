
exam_scores = {
    '张三': 85,
    '李四': 58,
    '王五': 72,
    '赵六': 45,
    '孙七': 90,
    '周八': 55
}
homework_grades = {
    '张三': 'A',
    '李四': 'B',
    '王五': 'C',
    '赵六': 'A',
    '孙七': 'B',
    '周八': 'A'
}
#一定要把等级转化成分数，这里可以用到自定义函数
def grades_to_scores(grades):
    if grades == 'A':
        return 90
    elif grades == 'B':
        return 80
    elif grades == 'C':
        return 70
    else:
        return 0

final_scores = []
students = []
#方便查询学生跟成绩的对应关系
students_scores = dict()
#为啥要遍历学生名字呢？
#遍历了学生名字，一方面这题中给的两个字典中，键都是学生名字，遍历学生名字方便后面查询信息
#另一方面，遍历学生名字也是为了下面创建学生名字的列表
for student in exam_scores.keys():
    students.append(student)
    #这个可以说是一些函数的嵌套，比较麻烦的是要分清变量之间的关系
    #还有，这里调用了上面定义的函数，以及字典中的查询（通过键来查找值）
    usual_scores = grades_to_scores(homework_grades[student])
    #这一个跟上面一样都是字典的查找，只不过没有那么麻烦
    exam_score = exam_scores[student]
    final_score = exam_score*0.7+usual_scores*0.3
    #把最终成绩放入列表中，方便后续打包组装成字典
    final_scores.append(final_score)

    #学生的名字以及对应的最终成绩
students_scores = dict(zip(students, final_scores))
#平均分
average = sum(final_scores)/len(final_scores)
extra_students = []
#这一个遍历跟上面的一样
for name in exam_scores:
    #下面这两行就是字典的通过键来获得值
    #字典也可以遍历啊，只不过遍历结果默认的是键
    homework_grade = homework_grades[name]  # 平时评级
    exam = exam_scores[name]  # 期末成绩
    #因为有优先级，所以可以加上一个小括号
    if (homework_grade == 'A' or homework_grade == 'B') and exam < 60:
        extra_students.append(name)
        #调侃一句，在这整串代码中，应该就属文件写入最简单了
with open('grade_report.txt','w',encoding = 'utf-8')as f:
    f.write(f'每个学生的最终成绩：{students_scores}')
    f.write(f'\n平均分：{average}')
    f.write(f'\n需要单独发的学生名单：{extra_students}')
