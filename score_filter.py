scores = [88, 59, 92, 45, 76, 60, 55, 83]
count = 0
sum1 =0#在现在这个for循环里面，也可以根据需要来设定一个计数器
for i in scores:
    if i >= 60:
        count += 1
    sum1 += i#这是一个求列表内元素总数的方法，但是也可以直接sum(scores)，这样直接可以得出列表内元素的相加之和
print(count)#这个输出最好不要在循环里面，不然会一直输出count的值，直到结束
average = sum1 / len(scores)#设一个变量，来表示平均值
print(f'{average:.1f}')#变量名：.数字f 这个形式的确是可以保留小数但必须是在f格式化中才可以用并且要在 变量名：.数字f 的前后都加上花括号
