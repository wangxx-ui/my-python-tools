book1 = ('《Python编程》', '张三', 59.9, '清华大学出版社')#创建一个元组
print(book1)
book1_name = book1[0]#根据元组内元素的索引来获得该索引位置的元素
book1_price = book1[2]#同上
print(f'{book1_name}的价格是{book1_price}元')#借助f格式化表达来进行不同类型字符的结合
print(book1[0:3])#这个是切片，从索引为0开始包括位置为0的元素，到了3结束，但是不包括索引位置为3的元素
# book1[0] = 'Java编程'#这个报错了，至于报错的原因是，元组有内部元素不可变的性质
book1 = list(book1)#这是一个把元组变成列表的操作
book1[0] = 'Java编程'#由于元组内部元素不可变，那么就有必要先把元组转化成列表再进行定向位置的元素内容转化
print(book1)
book1 = tuple(book1)#这个操作就是把列表转化为元组
print(book1)
book2=('数据分析', '李四', 69.9, '机械工业出版社')
library =[book1,book2]#元组合并成一个列表，如果把两个元组简单的相加，那么你只会获得毫无逻辑章法的一个乱元组，而如果你是吧两个元组合并成一个列表，那么各个元组的内容就不会乱
print(library)
print(len(library))#获取元组内的元素个数
new_book_name=input('请输入一本书的名字：')
if new_book_name in library:
    print(new_book_name)
else:
    print('这本书不在哦，亲')#上面的if函数就是进行一个条件讨论
count=0#下面开始一个for循环
for i in library:
    if i[2]<65:
        count=count+1
print(count)
print(f'\t图书馆总藏书量:{len(library)}\n\t价格低于65元的书的数量:{count}')
