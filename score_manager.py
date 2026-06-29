#创建初始成绩单
scores = [88, 92, 76, 65, 59, 83, 70, 95, 45, 78]
print(scores)
#统计成绩基本信息
print(len(scores))#获取成绩单的元素数量（学生人数）
print(scores.count(70))#获得成绩单中70这一个元素的数量
#向成绩单中添加新成绩
new_scores = int(input('请输入一个新的成绩（整数）：'))
scores.append(new_scores)#把新变量加在列表的最后一个位置
new_scores1 = int(input('请输入一个新的成绩（整数）：'))
num = int(input('请输入新成绩的位置编码(整数)：'))
scores.insert(num,new_scores1)#一个新变量加在指定位置索引的位置
print(scores)
#删除成绩
del scores[0]#删除掉在0这个索引位置的元素
new_scores2 = int(input('请输入一个新成绩（整数）：'))
if new_scores2 in scores:
    scores.remove(new_scores2)#用一个if函数来讨论这一个新成绩是否在列表中，然后再分开讨论
print(scores)
#修改成绩
new_scores3 = int(input('请输入一个新成绩（整数）：'))
num2 = int(input('请输入其中你要修改成绩的位置编码'))
scores[num2] = new_scores3#这个是在num2这个索引位置上把一个新成绩覆盖在另一个老成绩上，也就是代替
print(scores)
#排序与查找
scores.sort(reverse=True)#把我们的成绩列表（因为是全为数字）按照降序来排序
print(scores)
address=scores.index(95)#这个是查找95在这个成绩列表里面的索引位置
print(address)
if 55 in scores:
    print(scores.index(55))
else:
    print('该分数不存在')#上面的if函数就是先判断55这个数字是否在成绩列表里面，然后再查找55的索引位置或者输出‘该分数不存在’
#格式化输出报告
print(f'\t当前学生人数:{len(scores)}\n\t最高分和最低分:{scores[0],scores[len(scores)-1]}\n\t分数为 70 的学生人数:{scores.count(70)}\n\t排序后的成绩单:{scores}')
