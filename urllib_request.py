import urllib.request
import urllib.parse
import json

# 爬取网页信息
html_url = "http://www.baidu.com"
html_resp = urllib.request.urlopen(html_url)

# 读取全部，读取一行可用readline()，多行返回列表的可用readlines()
html = html_resp.read() 
html = html.decode('utf-8')  # 解码
print(html)

# 获得其他信息：
html_resp.info() # 获得头相关的信息，HTTPMessage对象
html_resp.getcode() # 获得状态码
html_resp.geturl() # 获取爬取的url

# url中包含汉字是不符合URL标准的，需要进行编码
urllib.request.quote('http://www.baidu.com') 
# 编码后：http%3A//www.baidu.com

urllib.request.unquote('http%3A//www.baidu.com') 
# 解码后：http://www.baidu.com
