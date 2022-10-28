import requests


def get_proxy(num=10):
    res =[]
    for n in range(0,num):
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            res.append(response.text)
    return res

if __name__ == '__main__':
    PROXY_POOL_URL = 'http://localhost:5555/random'
    proxy_list = get_proxy()
    print(proxy_list)

