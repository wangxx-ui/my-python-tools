class pet:
    def __init__(self,name,kind,age):
        self.name = name
        self.kind = kind
        self.age = age
    def show_info(self):
        print(f'我的名字是{self.name},是一只{self.kind}，今年{self.age}岁了')
wangcai = pet('旺财','柴犬',3)
wangcai.show_info()
wanggou = pet('王狗','中华田园犬',2)
wanggou.show_info()
