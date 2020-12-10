import requests
from selenium import webdriver

print('1111')

headers = {"User-Agent":'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_6) AppleWebKit/537.36(KHTML,like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
#get html code
'''


response = requests.get(url = 'http://www.baidu.com',headers=headers)

print(response.content.decode('utf-8'))

print(response.text)

print(response.headers)

print(response.status_code)
'''

#get png code
'''
response =  requests.get(url='https://www.baidu.com/img/bd_logo1.png',headers=headers)

with open('C://Users/Tang Han/learngit/x230_office_pytest/baidu.png','wb') as f:
    f.write(response.content)
'''

#get JS sources

#response = requests.get(url='https://www.toutiao.com/',headers=headers)
#print(response.content)

chrome = webdriver.Chrome()

chrome.get('https://www.baidu.com')