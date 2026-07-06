products = list()#用list内置函数创建一个空列表
while True:
    product = input('请输入商品名称：')
    if product == 'quit':#当输入的商品名称是quit时，循环结束
        break
    products.append(product)#每输入一个商品名称时就会添加到列表的最后一位
print(products)
settings = ('v1.0', '默认仓库')
print(settings)
count2 = 0
for i in products:#此时的i是列表中的一个元素
    if len(i)>=3:#len(i)在这时就是i这个元素的长度
        count2 += 1
print(count2)
product2 = input('请输入商品名称：')
if product2 in products:
    print('存在')
else:
    print('不存在')
print(f'\t商品总数:{len(products)}\n\t名称长度≥3的商品数:{count2}\n\t版本号和仓库名:{settings}')
