import requests

# get请求
req_get = requests.get('https://www.baidu.com')
# post请求
req_post_1 = requests.post('https://www.kmqsaq.com/user/login',data={"clientType": 1, "userName": "15755384659", "password": "135781011"})
"""
# 其他请求:
r = requests.put('https://httpbin.org/put', data = {'key':'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')
# 携带参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
"""
# 假装是浏览器
url = f'https://www.kmqsaq.com/user/login'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
req_post_2 = requests.post('https://www.kmqsaq.com/user/login',headers=header,data={"clientType": 1, "userName": "15755384659", "password": "135781011"})
# 获取文本内容
print(req_post_2.text)
# 获取字节响应内容
print(req_post_2.content)
# 获取响应码
print(req_post_2.status_code)
# 获取响应头
print(req_post_2.headers)
# 获取json响应内容
print(req_post_2.json())
# 请求时以json为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.json())
# 获取cookies信息
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies['example_cookie_name'])
# 发送cookie信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)