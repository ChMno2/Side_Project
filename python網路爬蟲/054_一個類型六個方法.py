import urllib.request

url = 'http://www.baidu.com/'

#模擬瀏覽器向服務器發送請求
response = urllib  .request.urlopen(url)

#一個類型和六個方法
#response是http Response的類型
# print(type(response))  # <class 'http.client.HTTPResponse'>

#按照一個字節一個字節的讀
# content = response.read()
# print(content)

#返回多少個字節
# content = response.read(5)
# print(content)

#讀取一行
# content = response.readline()
# print(content)

# #讀一整行直到讀完
# content = response.readlines ()
# print(content)

# #返回狀態碼 如果是200了 那麼就證明我們的邏輯沒有錯
# print(response.getcode())

#返回的是url地址
# print(response.geturl())

#獲取的為一個狀態信息
print(response.getheaders())

#一個類型HTTP response
#六個方法 read readline readlines getcode getheaders geturl
