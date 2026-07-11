records= []
#定义一个函数
#括号里面的records是用来命令数据都必须是加到records里面
def add_income(records, amount, description):
    #函数内容是把下面这个字典按照这个格式添加到上面那个空列表中
    record = {'type': '收入', 'amount': amount, 'description': description}
    records.append(record)
    #同上
def add_expense(records, amount, description):
    record1 = {'type': '支出', 'amount': amount, 'description': description}
    records.append(record1)
    #定义一个叫 计算结余的函数
    #括号里面的records是计算records里面的东西，括号里面必须有records
def calculate_balance(records):
    #定义两个变量，总收入，总支出
    total_income = 0
    total_expense = 0
    #遍历records这个列表，record是字典
    for record in records:
        #if条件
        if record['type']=='收入':
            total_income += record['amount']
        if record['type']=='支出':
            total_expense += record['amount']
    balance1 = total_income - total_expense
    #计算出结果要么return，要么设置一个变量接住这个结果
    return  total_income, total_expense,balance1
#调用函数并输出结果
#要先调用，需要先定义变量，要有东西接住它们
income,expense,balance2 =  calculate_balance(records)
print(f'总收入：{income},总支出：{expense},结余：{balance2}')

def batch_add_income(records, *amounts):
    for amount in amounts:  # 遍历每个金额
        add_income(records, amount, '批量收入')  # 复用已有函数
#调用函数，并输出
batch_add_income(records, 666,999,90909)
while True:
    print("""text
1. 添加收入
2. 添加支出
3. 查看统计
4. 退出""")
    a = int(input('请根据菜单以及想要使用的工具来输入数字：'))
    if a == 1:
        x = float(input('请输入数量：'))
        y = input('请输入描述：')
        #调用这个函数不需要输出，因为这属于是直接在外部更改内部信息
        add_income(records,x, y)
    if a == 2:
        x =float(input('请输入数量：'))
        y = input('请输入描述：')
        #同上
        add_expense(records, x, y)
    if a == 3:
        income, expense, balance2 = calculate_balance(records)
        print(f'总支出：{income},总收入：{expense},结余：{balance2}')
    if a == 4:
        break
