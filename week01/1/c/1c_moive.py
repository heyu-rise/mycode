import requests
import lxml.etree
import pandas

url = 'https://movie.douban.com/subject/1292052/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/78.0.3904.108 Safari/537.36 '
header = {'user-agent': user_agent}
response = requests.get(url, headers=header)
selector = lxml.etree.HTML(response.text)

mylist = []

file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称{file_name[0]}')
mylist.append(file_name[0])

movie1 = pandas.DataFrame(data=mylist)
movie1.to_csv('./movies1.scv', encoding='utf-8', index=False, header=False)