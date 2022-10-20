from urllib import request, parse
import ssl

# 对于https,使用未经验证的上下文
context = ssl.create_default_context()
url = f'https://www.kmqsaq.com/user/login'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
request_param = {"clientType": 1, "userName": "15755384659", "password": "135781011"}
request_param_parse = bytes(parse.urlencode(request_param),'utf-8')
# 封装request
req = request.Request(url,data=request_param_parse,headers=header,method='POST')
# 获取响应
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))