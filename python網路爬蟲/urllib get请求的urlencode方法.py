
#urlencode應用場警:多個參數的時候
#https://www.google.com.tw/search?q=周杰倫&sex=男
# import urllib.parse
# data ={
#     'wd':'周杰倫',
#     'sex':'男',
#     'locdtion':'台灣'
# }

# a = urllib.parse.urlencode(data)

#https://www.google.com.tw/search?q=%E5%91%A8%E6%9D%B0%E5%80%AB&sex=%E7%94%B7&location=%E5%8F%B0%E7%81%A3

import urllib.parse
import urllib.request
base_url = 'https://www.google.com.tw/search?'
data ={
    'q':'周杰倫',
    'sex':'男',
    'location':'台灣'
}
new_data = urllib.parse.urlencode(data)
url = base_url+new_data

headers ={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

request = urllib.request.Request(url=url,headers=headers)
print(request)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
