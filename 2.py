#!/usr/bin/env python

from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IExtensionHelpers
from burp import IContextMenuFactory
from burp import IContextMenuInvocation

from javax.swing import JMenuItem

import threading,socket

class BurpExtender(IBurpExtender,IContextMenuFactory):

    def	registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("ScanOSinje")
        self.callbacks.registerContextMenuFactory(self)
        return

    def createMenuItems(self,invocation):
        menu_list = []
        menu_list.append(JMenuItem("ScanOSinje",None,actionPerformed= lambda x, inv=invocation:self.startThreaded(self.start_scan,inv)))
        return menu_list

    def startThreaded(self,func,*args):
        th = threading.Thread(target=func,args=args)
        th.start()

    def start_scan(self,invocation):
        http_traffic = invocation.getSelectedMessages()
        if len(http_traffic) !=0:
            print 111
            #service = http_traffic[0].getHttpService()
            http_service = http_traffic[0].getHttpService()
            request = http_traffic[0].getRequest()
            headers = http_traffic[0].getHeaders()
            parameters = http_traffic[0].getParameters()
            print http_service