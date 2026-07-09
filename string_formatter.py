name = input('请输入你的名字：')
name = name.strip()#对姓名进行去除首尾空格处理
phone = input('请输入你的手机号：')
mail = input('请输入你的邮箱：')
print(phone.isdigit())#判断手机号是否全为数字
print('@' in mail)#判断@是否在邮箱中
s = input('请随机输入一段话：')
print(s.replace(' ','-'))#把句子中的空格转化为一个短横
print(s.replace(' ','-').split('-'))#把上面那个转化后的字符串在进行一个操作
#这样做我感觉更方便，但是容易看不懂吧
s1 = input('请输入一个英语单词：')
print(s1.lower())#把字母全转化为小写
print(s1.upper())#把字母全转化为大写
s2 = input('请输入一个句子：')
print(s2.count('a'))#统计a在s2中的出现次数
print(s2.find('a'))#查找a的位置，如果存在，输出索引位置，如果不在，输出-1
print(f'\t清洗后的姓名:{name}')
print(f'\t手机号是否全为数字:{phone.isdigit()}')
print(f"\t邮箱是否包含@：{'@' in mail}")
print(f"\t替换后的句子:{s.replace(' ','-')}")
print(f'\t大写单词:{s1.upper()}')
print(f'\t小写单词:{s1.lower()}')
print(f"\ta 的出现次数和首次出现位置:{s2.count('a'),s2.find('a')}")
