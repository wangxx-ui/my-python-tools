temp1 = int(input('请输入当前温度（整数）：'))
if temp1 > 38:
    print('红色预警：极端高温')
elif  38 >= temp1 >= 35:
    print('橙色预警：高温')
elif temp1 < 0:
    print('蓝色预警：低温')
else:
    print('温度正常')
scores = [88, 59, 92, 45, 76, 60, 55, 83]
new_scores1 = list(map(lambda x:x+5, scores))
print(new_scores1)
#需要注意的一点是，可以看出来，我下面写的函数其实是要跟filter结合判断的，
#所以，我们本应该有一个if条件判断
#反正我按照我的道理推应该是这样的，但是在这个情况下，不能用if应该直接返回
#其实这样做得到的结果其实是bool类型，但因为filter是直接把True的类型放到我们的新列表中，所以并不冲突
# def panduan(x):
#     return x>=60
# new_scores2 = list(filter(panduan, new_scores1))
new_scores2 = list(filter(lambda x:x>=60, scores))
print(new_scores2)
#现在一个工具箱里取出reduce这个函数
from functools import reduce
#应用reduce函数
total = reduce(lambda x,y:x+y,scores)
print(total)
students =dict()
while True:
    name = input('请输入学生姓名：')
    if name == 'quit':
        break
    score = int(input('请输入学生成绩（请输入时取整）：'))
    students[name] = score
def analyze_students(students1):
    num1 = 0
    total_score1 = 0
    average_score1 = 0
    for student in students1.items():
        num1 +=1
        total_score1 += student[1]
        average_score1 = total_score1/num1
    top1_name1 = max (students.items(),key =lambda x:x[1])
    return num1, average_score1,top1_name1[0]
num,average_score,top1_name = analyze_students(students)
print(f'\t学生总人数:{num}\n\t平均成绩:{average_score:.1f}\n\t最高分学生姓名:{top1_name}')
