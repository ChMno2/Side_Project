from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


url = 'https://rent.591.com.tw/'

browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

#找到輸入框

search_section = browser.find_element(By.XPATH,'//*[@id="rent-list-app"]/div/section[1]/div[3]/input')
print("找到輸入框")
#輸入淡水區的文字
search_section.send_keys('淡水區')
print('列出淡水區文字')
time.sleep(3)
#找到點擊按鈕
search_button = browser.find_element(By.XPATH,'//*[@id="rent-list-app"]/div/section[1]/div[3]/div')
print("找到搜尋送出按鈕")
#點擊搜尋按鈕
search_button.click()
print("按下按鈕")
time.sleep(3)
#找到獨立套房的位置
rent_tao = browser.find_element(By.XPATH,'//*[@id="rent-list-app"]/div/div[2]/section[2]/ul/li[3]')
#點擊獨立套房的按鈕
rent_tao.click()
print('點擊套房按鈕')
time.sleep(3)
#找到5000元以下的選項
rent_fee = browser.find_element(By.XPATH,'//*[@id="rent-list-app"]/div/div[2]/section[3]/ul/li[2]/i')
#點擊該選項
rent_fee.click()
print('點擊5000元以下按鈕')
time.sleep(3)

#time.sleep()
#顯式等待
#隱式等待
content = browser.find_element(By.XPATH,'//*[@id="rent-list-app"]/div/div[3]/div[1]/section[3]/div')
sections = content.find_elements(By.XPATH,'./section')

rent_list = []
for section in sections:
    rent_info = {}
    href = section.find_element(By.XPATH,'./a').get_attribute('href')
    full_text = section.find_element(By.CLASS_NAME,'rent-item-right').text
    price_text = section.find_element(By.CLASS_NAME,'item-price-text').text
    rent_info['href'] = href
    rent_info['full_text'] = full_text
    rent_info['price_text'] = price_text
    rent_list.append(rent_info)
print(rent_list)
