comment = input('请输入评论：')
if len(comment) >= 5:
    print('有效评论')
else:
    print('无效评论，请重新输入')
comments = [
    "非常好用，强烈推荐！",
    "一般般，不是很满意",
    "质量太差了，后悔买",
    "物流很快，包装完好",
    "还不错，价格也合适",
    "差评，完全不值这个价",
    "超级喜欢，下次还会再来"
]
#len函数不是统计列表的元素个数吗？啥时候是直接统计列表内部元素的长度了
#现在解释，map函数是可以直接遍历comments这个列表中的元素的，所以x就是代表comments里面的元素了
comments_num = list(map(lambda x :len(x), comments))
print(comments_num)
good_comment = list(filter(lambda x : '好' in x or '推荐' in x  or '喜欢' in x, comments))
print(good_comment)
#先取出reduce
from functools import reduce
#要加就加字符串的个数，不要直接把原本的那个列表放里面，不然加的就会是字符串
total = reduce(lambda x, y : x + y, comments_num)
print(total)
all_comments = []
print('注意：当输入quit时，将停止录入数据')
while True:
    comment2 = input('请输入评论：')
    if comment2 == 'quit':
        break
    all_comments.append(comment2)
def analyze_comments(comments1):
    good_comment1 =0
    for comment1 in comments1:
        if '好' in comment1  or '推荐' in comment1  or '喜欢' in comment1:
            good_comment1+= 1
    good_comment_rate = good_comment1 / len(comments1)
    return len(comments1), good_comment1, good_comment_rate
#原本应该是直接用别的变量名去承接这个元组中的元素的，但是因为局部变量的原因，所以没啥大问题
len_comments, good_comment1, good_comment_rate = analyze_comments(all_comments)
print(f'\t评论总数：{len_comments}\n\t好评数量：{ good_comment1}\n\t好评率：{ good_comment_rate:.1f}')
