# coding: utf-8
'''
@author: guimaizi
'''
from burp import IBurpExtender
from burp import IContextMenuFactory
from burp import IBurpExtenderCallbacks
from burp import IContextMenuInvocation
from burp import IHttpRequestResponse
from javax.swing import JMenuItem
import os,json,subprocess

class BurpExtender(IBurpExtender,  IContextMenuFactory):
    
    def registerExtenderCallbacks(self, callbacks):
        self._actionName = "test_vul"
        self._helers = callbacks.getHelpers()
        self._callbacks = callbacks
        callbacks.setExtensionName("test_vul")
        callbacks.registerContextMenuFactory(self)
        return 

    def createMenuItems(self, invocation):
        menu = []
        responses = invocation.getSelectedMessages()
        if len(responses) == 1:
            menu.append(JMenuItem(self._actionName, None , actionPerformed= lambda x, inv=invocation: self.Action(inv)))
            return menu
        return None

    def Action(self, invocation):
        request = invocation.getSelectedMessages().pop()
        analyzedRequest = self._helers.analyzeRequest(request)
        url = analyzedRequest.url
        body = ""
        cookie = ""
        referer = ""
        useragent = ""
        Accept=""
        Content_Type=""
        headers = analyzedRequest.getHeaders()
        for header in headers:
            if header.startswith("Cookie: "):
                cookie = header.replace("Cookie: ","")
            elif header.startswith("Referer: "):
                referer = header.replace("Referer: ","")
            elif header.startswith("User-Agent: "):
                useragent = header.replace("User-Agent: ","")
            elif header.startswith("Accept: "):
                Accept = header.replace("Accept: ","")
            elif header.startswith("Content-Type: "):
                Content_Type = header.replace("Content-Type: ","")
            elif header.startswith("Content-type: "):
                Content_Type = header.replace("Content-type: ","")
        method=0
        if analyzedRequest.getMethod() == "POST":
            body = request.getRequest().tostring()[analyzedRequest.getBodyOffset():]
            method=1
        path="E:/hack/burp_lib"
        test_vul = "%s/test_vul.py"%path        
        data={"method":method,"Content_Type":str(Content_Type),"url":str(url),"post":str(body),"cookie":str(cookie),"useragent":str(useragent),"referer":str(referer),"Accept":str(Accept)}
        print data
        with open('%s/tmp.json'%path, 'w') as json_file:
            json_file.write(json.dumps(data))
        #subprocess.call('python3 /Users/guimaizi/hack-tool/burp_lib/test_vul.py')
        os.system('start cmd /k python %s'%test_vul)
        #os.system('ping dasda111.zk3qno.ceye.io')