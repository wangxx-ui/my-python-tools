# 背景：你正在帮一个运维团队分析服务器日志，需要从日志中提取关键信息。
#
# 任务一：用 match 检查日志格式
#
# 定义一个字符串 log1 = "[2025-08-07 14:30:25] ERROR: Disk usage exceeded 90%"
#
# 用 re.match 检查 log1 是否以 [ 开头。如果匹配成功，打印“日志格式正确”。
#
# 任务二：用 search 提取第一个时间戳
#
# 定义一个字符串 log2 = "Backup completed at 2025-08-07 15:00:00, next backup scheduled at 2025-08-08 03:00:00"
#
# 用 re.search 找出 log2 中第一次出现的时间戳（格式为 年-月-日 时:分:秒），并打印出来。
#
# 任务三：用 findall 提取所有IP地址
#
# 定义一个字符串 log3 = "Access from 192.168.1.1 and 10.0.0.5, failed login from 192.168.1.100"
#
# 用 re.findall 提取 log3 中所有的IP地址，并打印出来（结果应该是一个列表）。
#
# 任务四：用捕获组提取关键信息
#
# 定义一个字符串 log4 = "User admin logged in from 192.168.1.1 at 2025-08-07 14:30:25"
#
# 用 re.search 和捕获组，同时提取出用户名（admin）、IP地址（192.168.1.1）和时间戳（2025-08-07 14:30:25），并分别打印出来。
#
# 提示：你需要构建一个带有三个捕获组的正则表达式，分别捕获用户名、IP和时间戳。
#
# 任务五：添加注释
# 为每个功能块添加清晰的注释，说明这段代码在做什么。
import re
log1 = "[2025-08-07 14:30:25] ERROR: Disk usage exceeded 90%"
if re.match(r'^\[', log1):
    print('日志格式正确')
else:
    print('日志格式不正确')

log2 = "Backup completed at 2025-08-07 15:00:00, next backup scheduled at 2025-08-08 03:00:00"
res = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log2)
#在match，search这些的函数中res.group()，这样写可以直接转化为数字
print(f'第一个时间戳：{res.group()}')

log3 = "Access from 192.168.1.1 and 10.0.0.5, failed login from 192.168.1.100"
#如果想要获得列表中的元素也可以按照之前索引的方式查找列表中对应的元素   下面这个是索引第一个元素，以此类推
# res1 = re.findall(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', log3)[0]
res1 = re.findall(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', log3)
print(f'IP地址：{res1}')

log4 = "User admin logged in from 192.168.1.1 at 2025-08-07 14:30:25"
res2 = re.search(r'User (\w+) logged in from ((?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)) at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', log4)
#在group这个函数中一般打扮的种类信息，可以在括号中不添加任何符号
#但是如果有多种类的信息的话那就，需要像下面这样分组了
print(f'用户名：{res2.group(1)}')
print(f'IP地址：{res2.group(2)}')
print(f'时间戳：{res2.group(3)}') 
