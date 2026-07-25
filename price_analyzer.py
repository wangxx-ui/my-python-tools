#仍然是练手的作业，也就是可以当作我的学习历程一样的东西
tem = int(input('请输入今天的室外温度（要求是整数）：'))
if tem >35:
    print('太热了，注意防暑')
elif tem<10:
    print('太冷了，注意保暖')
else:
    print('温度适宜')
#猜数字
while True:
    num = input('请输入你猜的数字：')
    if num == 6:
        print('恭喜你，猜中数字了！')
        break
    else:
        print('猜错了哦，请再试一次。')
def  circle_area(r):
    return 3.14*r*r
#想要完成上面的函数定义，也可以是：
def circle_area1(r):
    result = 3.14*r*r
    return result
#也可以是：
def circle_area2(r):
    result = 3.14*r*r
    print(result)
    #关于半径，一定要是数字，因为字符串不能进行数字的运算
r1 = float(input('请输入圆的半径（要求数字）：'))
print(circle_area(r1))
products = {}
while True:
    goods1 = input('请输入商品名称：')
    if goods1=='quit':
        break
    price1 = int(input('请输入商品的价格（整数）：'))
    #直接在字典中添加对应的值和键，比先把两个列表打包在合并成一个字典 要简单得多。还有，如果用后者的方法的话，就会有一点是上面定义的空字典会有一点黄色警告，不美观吧（我个人感觉）
    products[goods1]=price1
    #括号里面只是一个变量名，为了更方便他人以及以后的自己看懂
def calc_total(prod_dict):
    total = 0
    #.values()这个是在字典中的专用函数，用来查找字典中的值
    for price2 in prod_dict.values():
        total += price2
    return total
#price这个列表也可以用，但是在这里是为了代码更加整洁明了，是脱离脚本小子的关键一步！
max1 = max(products.values())
print(max1)
print(f'\t商品总价:{calc_total(products)}\n\t最贵商品的价格:{max1}')
