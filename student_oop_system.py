class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        #现在才知道，大部分的类中的方法括号里面的参数用self一个就够了
    def get_average(self):
        num = 0
        total = 0
        #默认遍历的是字典中的键
        for score in self.scores:
            num +=1
            total += self.scores[score]
            average = total / num
        return average
class ClassRoom:
    def __init__(self):
        #规定好在每创建一个Classroom的对象时，都自动生成一个空列表
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def get_all_average(self):
        # self.averages = averages 这个是写错了
        total = 0
        for student in self.students:
            #这个是先把Student中的对象放到Classroom中然后可以在Classroom中用Student的方法
            #还不用继承
            total += student.get_average()
        return total/len(self.students)
        # averages.append(student.get_average())  同上
        # all_average = sum(averages)/len(averages)
        # return all_average
    def get_excellent_students(self):
        excellent_students = []
        for student in self.students:
            #用抽象的变量来表示数量
            if student.get_average() > 85:
                #student.name  这个也是相当于在Classroom中使用Student这个类创建的对象的方法
                excellent_students.append(student.name)
        return excellent_students
stu1 = Student('xiaoming',{'语文':88,'数学':90})
stu2 = Student('xiaohua',{'语文':80,'数学':91})
stu3 = Student('maomao',{'语文':50,'数学':71})
classroom = ClassRoom()
classroom.add_student(stu1)
classroom.add_student(stu2)
classroom.add_student(stu3)
print(f'全班平均分:{classroom.get_all_average():.2f}')
print(f'优秀学生名单:{classroom.get_excellent_students()}')
#在文件student_report.txt中保存
with open('student_report.txt', 'w', encoding='utf-8') as f:
    f.write(f'全班平均分:{classroom.get_all_average():.2f}')
    f.write('\n')
    f.write(f'优秀学生名单:{classroom.get_excellent_students()}')  
