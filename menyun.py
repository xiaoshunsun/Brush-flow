import requests

headers1 = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}

data1 = {
  'email': '9916765@qq.com',
  'passwd': 'sunxs241@'
}

response1 = requests.post('https://www.cutecloud.net/auth/login', headers=headers1, data=data1)
cookies = response1.cookies.items()
cookie = ''
for name, value in cookies:
    cookie += '{0}={1};'.format(name, value)
    
headers2 = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'cookie': cookie,    
}

data2 = {
  'coupon': '',
  'shop': '22',
  'autorenew': '0',
  'disableothers': '1'
}

response2 = requests.post('https://www.cutecloud.net/user/buy', headers=headers2, data=data2)
json =  response2.json()
print(json)
