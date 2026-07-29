words = input('请输入一句你想说的话：')
#先写入
with open('diary.txt','w',encoding = 'utf-8')as f:
    f.write(words+'\n')
    print('日记已保存')
#再追加
words1 = input('请输入一句你想说的话：')
with open('diary.txt','a',encoding = 'utf-8') as f1:
    f1.write(words1+'\n')
    print('日记已追加')
#最后读取
with open ('diary.txt','r') as f2:
    words_list = f2.readlines()
for word in words_list:
    print(word.strip())
#因为words_list现在是个列表，用len函数可以获取列表元素个数
num = len(words_list)
total = 0
#现在i就是words_list这个列表中的元素，对元素用len函数在进行累加，可以得出结果
#当然也可以用reduce函数
# from functools import reduce
# #但但对于字符串可以用len函数去求长度   ，不能用sum函数，这个一般用来求列表中数据的总数
# total_list = list(map(lambda x:len(x),words_list))
# total = reduce(lambda x,y:x+y,total_list)
# print(total)
for i in words_list:
    x = len(i)
    total += x
print(f'\t日记总行数:{num}\n\t总字符数:{total}')
