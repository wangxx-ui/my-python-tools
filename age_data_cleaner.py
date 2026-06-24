#先获得数据集合
ages = [25, -5, 18, 0, 120, 55, 200, 30, 17, 45, -3, 60]
#然后创造两个变量来分别盛放不同数据
valid_ages = []
invalid_ages=[]
#再开始for循环
for i in ages:
    #循环内部if函数常见的手法
    if 0<i<=120:
        valid_ages.append(i)#这个是吧符合条件的i放到对应的变量中
    elif i==0:
        continue
    else:
        invalid_ages.append(i)
#之后，开始完成另一个任务
average_valid_ages = sum(valid_ages)/len(valid_ages)#sum(集合)：一个集合的数量总和，len(集合)：一个集合内部的元素个数
#最后打印
print(f'\t有效年龄列表：{valid_ages}\n\t无效年龄列表：{invalid_ages}\n\t有效年龄平均值：{average_valid_ages:.1f}')
