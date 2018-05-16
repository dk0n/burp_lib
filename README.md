# 简单便捷的burp插件 #
因为burp Scanner不能设置攻击参数，我这个保存burp截取的http/s请求数据为tmp.json文件(目前只支持get、post请求)，遍历http/s请求包参数值,追加漏洞检测代码在参数之后  
burp_vul.py(导入进burp的插件)  导出burp截取的http/s请求数据保存至tmp.json文件  
test_vul(漏洞检测插件)为测试漏洞代码  