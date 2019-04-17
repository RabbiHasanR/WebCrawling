import requests
import re

url='http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

response=requests.get(url)
if response.ok==True:
    text=response.text
    text=text.replace('\n',' ')
    book_pat=re.compile(r'<h3><a href="(.*?)"\s*title="(.*?)"') # findall book using regex
    next_page_pat=re.compile(r'<li class="next"><a href="(.*?)">next</a></li>')
    result_next_page=re.findall(next_page_pat,text)
    print(len(result_next_page))
    print(result_next_page)
    result_book=re.findall(book_pat, text)
    print(len(result_book))
    print(result_book[0])