# coding: utf-8
'''
Created on 2018��4��18��

@author: 63571
'''
import requests
#r = requests.get('https://www.baidu.com')
'''kv={'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0','cookie':'asda=dsadas',"Content-Type": "application/x-www-form-urlencoded"}
r = requests.post('http://192.168.0.136/test_vul.php?aasdas=dsadas&xss=aa&13dsada=dsa',data='post_vul=dasxsssda',headers=kv)
print(r.text) '''
url='http://192.168.0.136/test_vul.php?dasd=!'.split('?')
if len(url)==1  or url[1]=='':
    print(1111)
print('http://192.168.0.136/test_vul.php?'.split('?'))