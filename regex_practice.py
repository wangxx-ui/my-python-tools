我直接把# 背景：你正在帮一个客服团队分析用户反馈，需要从一堆评论中提取关键信息。
#
# 任务一：用 match 检查开头
#
# 定义一个字符串 text1 = "2024年新款手机发布，非常值得购买"
#
# 用 re.match 检查 text1 是否以数字开头。如果匹配成功，打印匹配到的数字部分。
#
# 任务二：用 search 查找第一个数字
#
# 定义一个字符串 text2 = "这款手机的售价是1999元，非常划算"
#
# 用 re.search 找出 text2 中第一次出现的数字，并打印出来。
#
# 任务三：用 findall 提取所有数字
#
# 定义一个字符串 text3 = "我购买了3件商品，总价是299元，优惠了50元"
#
# 用 re.findall 提取 text3 中所有的数字，并打印出来（结果应该是一个列表）。
#
# 任务四：综合实战 - 提取邮箱地址
#
# 定义一个字符串 text4 = "请联系客服：support@example.com 或者 admin@test.org"
#
# 用 re.findall 和合适的正则表达式，提取出 text4 中所有的邮箱地址，并打印出来。（提示：邮箱地址的模式是 字母数字@字母数字.字母，可以用 \w+@\w+\.\w+ 来匹配）
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释，说明这段代码在做什么。
import re
text1 = "2024年新款手机发布，非常值得购买"
match_res = re.match(r'\d+',text1)
print(match_res)

text2 = "这款手机的售价是1999元，非常划算"
search_res = re.search(r'\d',text2)
print(search_res)

text3 = "我购买了3件商品，总价是299元，优惠了50元"
findall_res = re.findall(r'\d+',text3)
print(findall_res)


text4 = "请联系客服：support@example.com 或者 admin@test.org"
#邮箱的通用正则表达式\w+@\w+\.\w+
result = re.findall(r'\w+@\w+\.\w+',text4)
print(result)
