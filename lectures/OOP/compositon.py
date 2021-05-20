class Book:
    def __init__(self):
        page1 = Page('This is content of page 1')
        page2 = Page('This is content of page 2')
        self.pages = [page1, page2]

class Page:
    def __init__(self, content):
        self.content = content

our_book = Book()
for page in our_book.pages:
    print(page.content)