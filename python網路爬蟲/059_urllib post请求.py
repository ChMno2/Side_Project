import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
data ={
    'kw':'spider'
}

#post請求的參數 必須要進行編碼
data = urllib.parse.urlencode(data).encode('utf-8')

#post請求的參數 是部會拼接在url的後面 而是需要放在請求對象訂製的參數中
request = urllib.request.Request(url=url,data=data,headers=headers)

#模擬瀏覽器向服務器發送請求
response = urllib.request.urlopen(request)

# print(response)

content = response.read().decode('utf-8')

#字符串 --->json對象
import json
obj = json.loads(content)
print(obj)


#post請求方式的參數必須編碼
#編碼之後必須調用encode方法
#參數釋放在請求對象訂製的方法中
