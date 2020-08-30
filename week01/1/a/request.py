import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/78.0.3904.108 Safari/537.36 '

header = {'user-agent': user_agent}

my_url = 'https://movie.douban.com/top250'

response = requests.get(my_url, headers=header)

print(response.text)
print(f'返回码是: {response.status_code}')
