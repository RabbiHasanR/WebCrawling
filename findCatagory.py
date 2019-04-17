import requests
import re

url='http://books.toscrape.com/index.html'
response=requests.get(url)

if response.ok==True:
    text=response.text
    # print('Length is:',len(text))
    # print(text)
    regex=re.compile(r'<div class="side_categories">(.*?)</div>',re.M|re.DOTALL) #regex for find all category html from text
    result=re.findall(regex,text)
    text2=result[0]
    catagory_pat=re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<',re.M|re.DOTALL) # regext for find catagory from text2
    result_catagory=re.findall(catagory_pat,text2)
    print('Length is:', len(result_catagory))
    print(result_catagory[0])
else:
    print('Invalid url')
