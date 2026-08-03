class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def show_info(self):
        print(f'书名为：{self.title}')
        print(f'本书的作者是：{self.author}')

#创建对象
book = Book('《Python编程：从入门到实践》','Eric Matthes')
book.show_info()
