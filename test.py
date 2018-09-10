'''
Created on 2018年9月7日

@author: rasca1
'''
# coding: utf-8
'''
Created on 2018��4��18��

@author: guimaizi
'''
import json,re,requests

class test:
    def __init__(self):
        '''burp_plugin'''
        f = open('E:/hack/burp_lib/tmp.json', 'r', encoding='utf-8')
        test=re.sub('\'','\"',f.read())
        self.data=json.loads(test)
        #print(self.data)
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
            self.method_get(str)
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
                self.method_post(str,self.data['body'])
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
            self.method_post(self.data['url'],params)
        
    def method_post(self,url,data):
        #print(url)
        try:
            kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
            r = requests.post(url,data,headers=kv)
            return r.text
        except:
            pass
    def method_get(self,url):
        try:
            kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
            r = requests.get(url,headers=kv)
            return r.text
        except:
            pass
    def start(self):
        print(self.data)
        '''if self.data['body']=='':
            #urllist=self.data['url'].split('?')
            self.get_data(self.vul_payload)
        else:
            self.post_data(self.vul_payload)'''
    def xss_injection(self):
        '''
        :payload xss测试参数
        '''
        payload=['<\'\"xssguimaizi>']
        print(self.data)
        if self.data['body']=='':
            #urllist=self.data['url'].split('?')
            self.get_data(payload[0])
        else:
            self.post_data(payload[0])
    def cmd_injection(self):
        '''
        :payload 命令注入测试参数
        '''
        payload=[]
        print(payload)
    def ssrf_fuzz(self):
        '''
        :payload ssrf测试参数
        '''
        payload=[]
        print(payload)
        
        
if '__main__' == __name__:
    item=test()
    item.start()