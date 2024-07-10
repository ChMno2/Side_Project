
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E5%80%AB
#獲取周杰倫網頁的代碼
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='

headers ={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

#將周杰倫三個字變成unicode編碼的格式
#需要依賴於urllib.parse

name = urllib.parse.quote('周杰倫')

url +=name


#請求對象的定制
request = urllib.request.Request(url=url,headers = headers)

#模擬瀏覽器向服務器發送請求
response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')


print(content)
