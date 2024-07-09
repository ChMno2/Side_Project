#使用urllib來獲取首頁的原碼
import urllib.request
#1.定義一個URL
url= 'http://www.google.com/'

#2.模擬瀏覽器向服務器發送請求
response = urllib.request.urlopen(url)


#3.獲取響應中的頁面中的原碼
#read方法 返回的是字節形式是二進制數據
#二進制 --> 字符 解碼 decode
content = response.read().decode('utf-8')  #解��成utf-8格式的字符

#4.print出來
print(content) 
