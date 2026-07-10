#加法
def add(a, b):
    # 需要返回计算值的话，那么就用return，如果是返回一段文字之类的输出语句那么就用print
    return a + b
#减法
def subtract(a, b):
    return a - b
#乘法
def multiply(a, b):
    return a * b
#除法
def divide(a, b):
    if b==0:
        print('除数不能为0')
        #在这串代码后面也要加上return，目的是直接停止函数，不然相当于无效代码
        return
    return a / b
#打包成元组，再对元组进行指令
def sum_all(*args):
    return sum(args)
#调用函数,并且返回输出值
print(sum_all(1,2,3))
#定义函数名
def show_info(**kwargs):
    #遍历kwargs中的键和值
    for key, value in kwargs.items():
        #然后再打印出来
        print(f'{key}={value}')
#调用函数
#使用的时候就直接在括号中写上键=值（除了数字和等号和键其他都最好带上引号）
show_info(name='张三', age=18, city='郑州')
#提前写好菜单，如果菜单在循环内部，那么就会每一次循环都会出现这个菜单
print("""text
    1. 加法
    2. 减法
    3. 乘法
    4. 除法
    5. 退出""")
while True:
    #定义几个变量，为了后面计算，以及用户通过输入数字来调用函数
    z = int(input('请根据菜单输入数字：'))
    if z==1:
        x = float(input('请输入你要计算的其中一个数字：'))
        y = float(input('请输入你要计算的其中一个数字：'))
        print(add(x, y))
    if z==2:
        x = float(input('请输入你要计算的其中一个数字：'))
        y = float(input('请输入你要计算的其中一个数字：'))
        print(subtract(x, y))
    if z==3:
        x = float(input('请输入你要计算的其中一个数字：'))
        y = float(input('请输入你要计算的其中一个数字：'))
        print(multiply(x, y))
    if z==4:
        x = float(input('请输入你要计算的其中一个数字：'))
        y = float(input('请输入你要计算的其中一个数字：'))
        print(divide(x, y))
    if z==5:
        break
