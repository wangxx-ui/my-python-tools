scores = (88, 92, 76, 65, 59)
print(scores)#输出这个元组
print(len(scores))#获得元组内的元素数量
print(max(scores))#获得元组内的最大值
print(min(scores))#获得元组内的最小值
# scores[2]=80#为什么这行代码会报错：元组有个内部元素不可变的性质，电脑不能运行这串代码
scores =list(scores)#把元组通过内置函数list()把元组转化为列表
scores[2]=80#定向改变列表中的元素
scores = tuple(scores)#把列表通过内置函数tuple()转化为元组
print(scores)
new_scores = int(input('请输入一个分数：'))#通过输入函数input()来获得用户信息
if new_scores in scores:#通过if函数来分别讨论两种情况（只不过在这个情景中不需要再讨论else的结果了）
    print(new_scores)
