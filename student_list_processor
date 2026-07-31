old_students = ['张三', '李四', '王五', '赵六']
new_students = ['王五', '赵六', '孙七', '周八']
students = set(old_students + new_students)
#因为有重复的学员名，所以要用到集合这个不能有重复的
total_students = len(students)
#接下来要求出真正的新学员名单
only_new = [x for x in new_students if x not in old_students]
print(only_new)
#以及要求出真正的老学员名单
only_old = old_students.copy()
print(only_old)
with open("student_report.txt", "w", encoding="utf-8") as f:
    f.write(f'总共的学员数量：{total_students}')
    f.write(f'\n老学员的名单：{only_old}')
    f.write(f'\n新学员的名单：{only_new}')
