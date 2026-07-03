numbers=list()#建立一个空列表，也可以是numbers=[]
#开始死循环
while True:
    num = int(input('请随即输入整数：'))
    if num==0:#这里要让num等于0，需要用==来连接
        break#刹车 用来下一个停止死循环的命令
    else:
        numbers.append(num)#这个添加函数的格式为：列表名.append(要添加的东西)
positive_count = 0
negative_count = 0
oshu_count = 0#设置一个变量，用来当作后续的计数容器
#分别根据各个条件的不同，来进行对应的计数
for i in numbers:
    if i >0:
        positive_count += 1
    if i<0:
        negative_count += 1
    if i%2==0:
        oshu_count += 1
print(oshu_count)
average = sum(numbers)/len(numbers)
print(f'{average:.2f}')#保留两位小数
print(max(numbers),min(numbers))#求最大与最小值
numbers.sort(reverse=True)#来把列表设置为降序
print(7 in numbers)#会以bool类型的形式输出
print(f'\t输入的总数字个数:{len(numbers)}\n\t正数的个数和负数的个数:{positive_count,negative_count}\n\t偶数的个数:{oshu_count}\n\t平均值{average:.2f}\n\t最大值和最小值:{max(numbers),min(numbers)}\n\t降序排列后的列表:{numbers}\n\t数字 7 是否存在于列表中:{7 in numbers}')
