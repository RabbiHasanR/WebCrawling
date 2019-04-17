url='http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

i=url.rfind('/')
print(i)
# url=url[0:i]
# print(url)
url=url[0:i+1]+'page-2.html'
print(url)