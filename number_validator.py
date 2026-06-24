#依旧是先编写计数器
total=0
valid_count=0
#接下来用到死循环
while True:
    usernum = input('请输入一系列数字：')#在循环中让用户输入数字，不然只输入一遍并且下面的代码都运行不了
    #第一个循环内条件，没有else，也不需要它
    if usernum=='':
        break
        # 判断输入是否为数字
    if not usernum.replace('.', '').isdigit():#这个有点超纲，我还没学到
        print('输入无效，请输入一个数字')
        continue
        #在输入数字后，再给数字一个从字符串到数字的转换（因为输出的一定是字符串啊，下面要跟数字进行比较，要进行数据类型的转换）
    num = float(usernum)#但这数据类型的转换也一定要在循环内部的
    #这些条件都不需要否定的输出结果
    if num<=0:
        print('请输入正数')
        continue
    if num>0:
        #循环更新计数器
        total+=num
        valid_count+=1
print(f'\t有效输入的数字个数：{valid_count}\n\t累加总和（保留两位小数）{total:.2f}')#依旧要进行打印总结
