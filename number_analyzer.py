#先用一个死循环的变式来获得总数以及个数
total = 0
count = 0
while True:
    x = input('请随机输入一个数字：')#一定要先输入然后再进行对字符串来一个浮点数的转化（因为直接转化为浮点数，你点空格，会直接报错）
    if x=='' :
        break
    else:
        a=float(x)
        total += a
        count += 1#242-251算是一个while循环的一个比较完善的流程了
#下面是用三目运算法来定义parity（汉语：奇偶性）
num1 = int(total)
parity = '偶数' if num1%2==0 else '奇数'
print(parity)#其实感觉在这里打印有点多此一举了，毕竟，后面还要再打印一次
#看看下面的数列中有关整除3的数
numbers = [12, 7, 9, 15, 8, 21, 10, 33, 18, 5]
count_div3=0
for i in numbers:
    if i==10:
        continue
    if i%3==0:
        count_div3+=1#257-263算是完整的for循环了
#下面是总结的打印环节
print(f'\t用户输入的数字累加总和（保留两位小数）:{total:.2f}\n\t用户输入的数字个数:{count}\n\t累加和取整后是奇数还是偶数:{parity}\n\t给定列表中能被3整除的数字个数:{count_div3}')#在这串代码中主要是保留两位小数的方法
