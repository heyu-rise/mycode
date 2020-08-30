import requests

s = requests.Session()

r = s.get('http://httpbin.org/cookies/set/sessioncookie/sorry')
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)

# 会话可以使用上下文管理器
with requests.Session() as s2:
    s2.get('http://httpbin.org/cookies/set/sessioncookie/not')
    r = s2.get('http://httpbin.org/cookies')
    print(r.text)
