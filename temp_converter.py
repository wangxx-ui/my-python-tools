def c_to_f(celsius):
    return celsius * 9/5 + 32
celsius1 = float(input('请输入摄氏温度：'))
print(c_to_f(celsius1))
def convert_both(temp):
    #返回的两个值将会以元组的形式出现
    return temp*9/5+32,temp+273.15
#下面的两个temp1都只是替换temp的一个变量，当然数字也可以，只是形式上的区别
temp1 = float(input('请输入摄氏温度：'))
#调用函数并输出
fahr_temp,kelvin_temp = convert_both(temp1)
print(f'华氏温度：{fahr_temp}')
print(f'开尔文温度 :{kelvin_temp}')
def no_return():
    #这是个空语句，不影响代码正常进行
    pass
print(no_return())
unit = 'C'
#全局变量在函数定义中也可以调用
def show_unit():
    print(unit)
show_unit()
