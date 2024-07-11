import requests
from bs4 import BeautifulSoup
import json

url = "https://www.ptt.cc/bbs/NBA/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.findAll("div", class_="r-ent")
data_list = []

for a in articles:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "沒有標題"
    data["標題"] = title

    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular

    date = a.find("div", class_="date")
    if date:
        date = date.text.strip()  # 去除日期文字中的多餘空白
    else:
        date = "N/A"
    data["DATE"] = date

    data_list.append(data)

with open("ptt_nba_data.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)

print("資料已經存儲存為 ptt_nba_data.json")

# print(data_list)
    # print(f"標題:{title} 人氣:{popular} DATE:{date}")

# # print(response.text)
# if response.status_code ==200:
#     with open('output.html','w',encoding ='utf-8') as f:
#         f.write(response.text)
#     print("寫入成功")
# else:
#     print("沒有抓到網頁")
