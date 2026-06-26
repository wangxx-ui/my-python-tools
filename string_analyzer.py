#开始获得用户信息和基本统计
words=input('请输入任意长度的句子：')
print(len(words),words.count('a'))#输出句子字符个数，以及句子中a的个数
#索引与切片
print(words[0],words[len(words)-1])#取最后一个字母len(变量) - 1 就是最后一个字符的正索引位置
print(words[-1])#从右往左数，那么就是右面最后一个
print(words[0:5],words[-3:])#正索引是前面的算上后面的不算，负索引是从-1开始，从右往左数，也是前包括后不包括
#步长切片
print(words[::2])#省略了开始和结束，就是从头到尾，但是获取的字符是每隔一个取一个
print(words[::-1])#这个就是省略了开始和结束，从-1开始到着结束
#序列操作
words1=input('请输入任意长度的字母：')#再次获得用户信息
print(words+words1)
print(words*2)
print('e' in words)
print('z'not in words)#判断对应字母是否在字符串中，返回bool类型
#查找首次出现位置
if 'o'not in words:
    print('字母o不存在于该句子中',-1,sep='')
else:
    print(words.index('o'))
#格式化输出报告
print(f"第一个句子的字符总数{len(words)}，字母a出现的次数{words.count('a')}，第一个句子的首字符和尾字符{words[0],words[len(words)-1]}，反转后的句子{words[::-1]}，两个句子拼接后的结果{words+words1}，字母 e 是否存在{'e' in words}，字母 o 首次出现的位置{words.index('o')}")
