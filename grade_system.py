scores = list()#用内置函数创建空列表
n = int(input('请输入学生人数：'))
for i in range(n):#循环n次
    score = float(input('请输入学生成绩：'))
    scores.append(score)#把score这个元素依次添加到scores这个空列表的末尾
print(scores)
print("""text
1. 查看所有成绩
2. 查看平均分
3. 查看最高分和最低分
4. 统计及格人数
5. 退出""")#涉及到多行字符串
average = 0#提前定义好变量，避免后续输出有 没有定义 这样的警告
jige_count=0
while True:
    num = int(input('请根据菜单输入对应的数字：'))#输入函数一定要在循环里，不然循环会失控
    if num==1:
        print(scores)
    elif num==2:
        average = sum(scores)/len(scores)
        print(average)
    elif num==3:
        print(max(scores),min(scores))
    elif num==4:
        for i in scores:
            if i>=60:
                jige_count += 1
        print(jige_count)
    elif num==5:
        break#上面5个条件判断，分别对应5个命令
print(f'\t所有成绩:{scores}\n\t平均分:{average:.1f}\n\t最高分和最低分:{max(scores),min(scores)}\n\t及格人数{jige_count}')
