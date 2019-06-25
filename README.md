# burp漏扫插件
### 介绍
burp应该是在座的诸位安全从业人员必用的测试工具,重放http/s请求包是burp最常用的功能.

xss案例:
```
<?php
    $domain=$_POST['domain'];
  if($domain){
	echo $domain;
  }else{
    $html='<form name="input" action="" method="post">
    domain: <input type="text" name="dasdas">
    <input type="text" name="domadsa112n">
    <input type="text" name="domain">
    <input type="submit" value="Submit">
    </form>';
    echo $html;
  }
?>
```
那么漏洞测试就是修改http请求包的参数.如sql、xss、命令执行测试,无非是在参数值后面追加payload，然后查看响应包判读是否存在漏洞,然而一个参数一个参数的测试真的很辛苦。  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625110336.png)
如图，手工测到最后一个参数，才发现xss  

不如写个脚本遍历参数值,让程序自动加上漏洞检测payload并且重放。  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625110651.png)
点击触发扫描。  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625110807.png)

判断响应包http响应大小与返回内容是否存在关键字，依次来判断漏洞是否存在。  

![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625111017.png)

请自行修改漏洞检测用payload,与分析响应包的内容。  


### 环境搭建

参考:Burpsuite插件的使用:https://www.freebuf.com/sectool/158005.html

win10/8/7/xp  
python3.5+  
>pip install requests

设置绝对路径:  
test_vul.py 25行  
burp_vul_plugin 59行  

1.下载http://www.jython.org/downloads.html   Download Jython 2.7.0 - Standalone Jar 版  
导入:  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625112127.png)

2.导入我的漏洞检测  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625112300.png)

然后就可以用了:  
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625112900.png)

### 码个代码不容易，大爷大妈行行好，赏碗鸡煲翅吧，希望有钱人打赏,万分感谢。
![](https://raw.githubusercontent.com/guimaizi/cloud/test/20190625113229.png)

![](https://raw.githubusercontent.com/guimaizi/cloud/test/img/20190301182006.jpg)
