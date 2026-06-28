#创建初始购物清单
shopping_list=['牛奶', '面包', '鸡蛋', '苹果', '香蕉']
print(shopping_list)
#向清单中添加物品
sth1=input('请输入一个新物品：')#input函数收集要加在清单中的物品
shopping_list.append(sth1)#用append函数来把上面收集到的物品添加到清单最后
sth2=input('请输入一个新物品：')
num1=int(input('请输入你的物品位置编号：'))
#上面的这两行是分别再次收集要添加到清单中的物品以及其位置索引
shopping_list.insert(num1,sth2)
print(shopping_list)
#删除清单中的物品
sth3=input('请输入一个你要删除的物品：')
#用if函数来讨论情况
if sth3 not in shopping_list:
    print('该物品不在清单中，无法删除')
else:
    shopping_list.remove(sth3)
#列表运算
new_items = ['酸奶', '饼干', '橙汁']
full_list = shopping_list+new_items
print(full_list)
double_list = shopping_list*2
print(double_list)
#格式化输出报告
print(f'\t当前购物清单的物品总数（用 len）{len(full_list)}\n\t清单中第一个物品和最后一个物品（用索引）{full_list[0] , full_list[len(full_list)-1]}\n\t拼接后的完整清单{full_list}')
