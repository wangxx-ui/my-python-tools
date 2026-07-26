while True:
    name = input('请输入用户名：')
    code = input('请输入密码：')
    if name == 'admin' and code =='123456':
        print('登陆成功')
        break
    else:
        print('用户名或密码错误')
scores = [88, 59, 92, 45, 76, 60, 55, 83]
count = 0
for score in scores:
    if score<60:
        count += 1
print(count)
#当然 ，关于算这个列表元素之和，也可以用for遍历，然后再逐个相加，但是sum()这个函数可以增加代码的整洁性
def average(list1):
    average1 = sum(list1)/len(list1)
    return average1
#在f格式化中，变量一定要加上花括号，不然会默认为字符串
print(f'{average(scores):.1f}')
products = [('apple', 5), ('banana', 12), ('orange', 8), ('grape', 3)]
sorted_products = sorted(products,key=lambda product: product[1])
print(sorted_products)
max_product =max(products,key=lambda product: product[1])
print(max_product)
#我服了，还没学高阶函数filter，所以就先用列表推导式来做这个吧
new_products = [product for product in products if product[1]>=8]
print(new_products)
inventory = dict()
goods_name = []
goods_num =[]
while True:
    goods_name1 = input('请输入商品名称：')
    if goods_name1 == 'quit':
        break
    goods_name.append(goods_name1)
    goods_num1 = int(input('请输入商品库存：'))
    goods_num.append(goods_num1)
inventory = dict(zip(goods_name,goods_num))
def analyze_inventory(inventory1):
        total1 = 0
        for i in inventory1.items():
            total1 += i[1]
        #inventory1.items() 返回的是以元组构成的列表，所以得到的也是一个元组
        max_goods1 = max (inventory1.items(), key=lambda item: item[1])
        return total1 ,max_goods1
#这就直接调用了上面的函数，然后把两个变量存到外部，可供调用
total,max_goods = analyze_inventory(inventory)
#因为max_goods是一个元组（包含商品名和库存数量），而题目要的是商品名
print(f'\t总库存数量:{total}\n\t库存最高的商品名:{max_goods[0]}')
