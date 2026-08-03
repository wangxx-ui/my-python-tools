#定义父类
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('动物在叫')
#定义子类
class Dog(Animal):
    def speak(self):
        #下面这两行也可以写成
        #super().speak()
        #print('汪汪汪')
        super().speak()
        return '汪汪汪'
#再定义一个子类
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
#创建对象
wangcai = Dog('wangcai')
print(wangcai.speak())
xiaomao = Cat('xiaomao')
xiaomao.speak()
