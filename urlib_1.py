import urllib.request
import urllib.parse
import json

html_url = "http://www.baidu.com"
html_resp = urllib.request.urlopen(html_url)

html = html_resp.read()
print(html)
