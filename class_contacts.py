contact = dict()#用内置函数创建空字典
key = ('name', 'phone', 'email')#创建一个键的列表
#开始收集用户信息
name1 = input('请输入你的名字：')
phone1 = input('请输入你的号码：')
email1 = input('请输入你的邮箱：')
value = [name1, phone1, email1]#将用户信息组成一个列表
contact = dict(zip(key,value))#先把两个列表打包，然后组成一个字典
print(contact)
contacts = []
#下面几个设置为0的变量，是因为在循环里设置的变量，出了循环不能用
name2 = 0
phone2 =0
email2 =0
while True:
    name2 = input('请输入你的联系人名字：')
    if name2 == 'quit':
        break
    phone2 = input('请输入你的联系人号码：')
    email2 = input('请输入你的联系人邮箱：')
    list1 = [name2, phone2, email2]
    dict1 = dict(zip(key,list1))#这个跟前面的用两个列表组装成字典一样
    contacts.append(dict1)#列表中独有的在末尾添加元素方式
print(contacts)
tags = set()#目前所学的唯一的创建空集合的方法
while True:
    contact_label = input('请输入联系人标签（如“同学”、“同事”、“家人”）：')
    if contact_label == 'quit':
        break
    tags.add(contact_label)#集合的添加元素方法
print(tags)
print(len(contacts))#获得列表中的元素的数目
#下面是先假设found是假，然后用if条件判断怎样found是真，并且把前面的假设found是假给覆盖掉
#之后再根据对于found的条件判断来完成操作
name3 = input('请输入你的联系人名字：')
found = False
for contact in contacts:
    if contact['name'] == name3:
        found = True
if found:
    print(contact)
if not found:
    print('该联系人不存在')
print(f"\t联系人总人数:{len(contacts)}\n\t所有标签:{tags}\n\t第一个联系人的姓名和电话:{contacts[0]['name'],contacts[0]['phone']}")
