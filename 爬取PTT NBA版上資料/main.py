import requests
from bs4 import BeautifulSoup
#https://www.ptt.cc/bbs/NBA/index.html

url = "https://www.ptt.cc/bbs/NBA/index.html"
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
response = requests.get(url,headers=headers)
soup =  BeautifulSoup(response.text,"html.parser")#parser解析器
articles = soup.findAll("div",class_="r-ent")
for a in articles:
    title = a.find("div",class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "沒有標題"

    popular = a.find("div",class_="nrec")
    if popular and popular.span.text:
        popular = popular.span.text
    else:
        popular = "N/A"


    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    print(f"標題:{title} 人氣:{popular} DATE:{date}")
# # print(response.text)
# if response.status_code ==200:
#     with open('output.html','w',encoding ='utf-8') as f:
#         f.write(response.text)
#     print("寫入成功")
# else:
#     print("沒有抓到網頁")