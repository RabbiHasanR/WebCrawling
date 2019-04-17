import requests
import re

url='http://books.toscrape.com/catalogue/the-exiled_247/index.html'
response=requests.get(url)
if response.ok==True:
    text=response.text
    text=text.replace('\n',' ')
    info_img_pat=re.compile(r'<div class="item active">\s*<img src="(.*?)"\s*alt="[\s\w]*"\s*/>\s*</div>')#') #<table class="table table-striped"></table>')
    book_info_img=re.findall(info_img_pat,text)
    print(len(book_info_img))
    print(book_info_img)
    info_des_pat=re.compile(r'<div id="product_description"\s*class="sub-header">\s*<h2>Product Description</h2>\s*</div>\s*<p>(.*?)</p>')
    book_info_dis=re.findall(info_des_pat,text)
    print(len(book_info_dis))
    print(book_info_dis)
    info_upc_pat = re.compile(r'<th>UPC</th><td>(.*?)</td>')
    book_info_upc = re.findall(info_upc_pat, text)
    print(len(book_info_upc))
    print(book_info_upc)
    info_price_pat = re.compile(r'<th>Price \(incl. tax\)</th>\s*<td>\D+([\d.]+?)</td>')
    book_info_price = re.findall(info_price_pat, text)
    print(len(book_info_price))
    print(book_info_price)
    info_avi_pat = re.compile(r'<th>Availability</th>\s*<td>(.*?)</td>')
    book_info_avi = re.findall(info_avi_pat, text)
    print(len(book_info_avi))
    print(book_info_avi)
