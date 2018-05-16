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
import os

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
        headers = analyzedRequest.getHeaders()
        for header in headers:
            if header.startswith("Cookie: "):
                cookie = header.replace("Cookie: ","")
            elif header.startswith("Referer: "):
                referer = header.replace("Referer: ","")
            elif header.startswith("User-Agent: "):
                useragent = header.replace("User-Agent: ","")
        if analyzedRequest.getMethod() == "POST":
            body = request.getRequest().tostring()[analyzedRequest.getBodyOffset():]
        test_vul = "E:/hack/burp_lib/test_vul.py"        
        cmd={"url":str(url),"body":str(body),"cookie":str(cookie),"useragent":str(useragent),"referer":str(referer)}
        print cmd
        fo = open("E:/hack/burp_lib/tmp.json", "w")
        fo.write(str(cmd))
        fo.close()
        os.system('start cmd /k '+test_vul)