import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/78.0.3904.108 Safari/537.36 '

header = {'user-agent': user_agent}

my_url = 'https://movie.douban.com/top250'

response = requests.get(my_url, headers=header)

bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for tag in tags.find_all('a'):
        print(tag)
        print(tag.get('href'))
        print(tag.find('span').text)
