# coding: utf-8
import json,requests
from urllib import parse

class test_vul:
    def __init__(self):
        self.time_out=10
    def attack_post(self,data):
        try:
            kv = {'User-Agent': data['useragent'], 'Cookie': data['cookie'], 'Referer': data['referer'],
                  "Content-Type": data['Content_Type'],"Accept":data['Accept']}
            r = requests.post(data['url'],data=data['post'], headers=kv, timeout=self.time_out)
            return r.text
        except Exception as e:
            print('1.0','error : %s--%s' % (data['url'],e))
    def attack_get(self,data):
        try:
            kv = {'User-Agent': data['useragent'], 'Cookie': data['cookie'], 'Referer': data['referer'],
                  "Content-Type": data['Content_Type'],"Accept":data['Accept']}
            r = requests.get(data['url'], headers=kv, timeout=self.time_out)
            return r.text
        except Exception as e:
            print('1.0','error : %s--%s' % (data['url'],e))
    def update_load(self):
        fw =open('E:/hack/burp_lib/tmp.json',encoding='utf-8')
        data=json.load(fw)
        self.get_input(data)
    def get_input(self,data):
        print(data)
        payload_list_url=['\'','"',"\\","<xsssguimaizi>"]
        for statu in ['url','post']:
            if statu=='post':
                statu_num=2
            else:statu_num=4
            str_parame=data[statu]
            bits = list(parse.urlparse(str_parame))
            qs = parse.parse_qs(bits[statu_num])
            for i in qs:
                para = qs[i][0]
                for payload in payload_list_url:
                    qs[i]=para+payload
                    print(i+' : '+qs[i])
                    bits[statu_num] = parse.urlencode(qs, True)
                    str_parame = parse.urlunparse(bits)
                    data[statu]=str_parame
                    if data['method']==1:
                        print(i+' : '+qs[i]+self.result_with(self.attack_post(data)))
                    else:
                        print(i+' : '+qs[i]+self.result_with(self.attack_get(data)))
                    qs[i]=para
                print('-'*20)
    def result_with(self,data):
        #print(data)
        if 'xsssguimaizi' in str(data):
            data=' --- length: '+str(len(data))+' --- XSS: 1'
        else:
            data=' length: '+str(len(data))
        return data
if __name__ == '__main__':
    item=test_vul()
    item.update_load()
    #data={'referer': 'http://192.168.0.107/xss_payload/1.php', 'method': 1, 'cookie': '', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.0 Safari/537.36', 'url': 'http://192.168.0.107:80/xss_payload/1.php', 'Content_Type': 'application/x-www-form-urlencoded', 'post': 'dasdas=dasddas&domadsa112n=dasda&domain=dasdasda1223131'}
    #print(item.attack_post(data))