
import urllib.request

 
url = 'https://www.baidu.com'


#url的組成
#http/https    www.baidu.com    80/443        S     wd=周杰倫    #
#____的協議          主機          端口號     路徑      參數      錨點
#http     80
#https    443
#mysql    3306
#oracle   1521
#redis    6379
#mongodb  27017

headers ={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# 因為urlopen方法不能存儲字典，所以headers不能傳遞過去
# 請求對象的定製
#注意 因為參數順序的問題 不能直接寫url 和headers 中間還有data 所以我們需要關鍵字傳遞參數
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content  = response.read().decode('utf8')

print(content)




