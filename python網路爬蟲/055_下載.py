import urllib.request

#下載一個圖片
# url_img = 'https://lh3.googleusercontent.com/F-5w9_fBEKbrc5EGm4IHZeFgDZ--JlPK-JtHRh1O17AgQOZYaVZ0Wp9QAvWLcYfhcnp4lruGqzwV1HnJmcnNsXjQuDVPYvBJ7Wc=w960-rj-nu-e365'
# urllib.request.urlretrieve(url=url_img,filename='lisa.jpg')

#下載網頁
url_page = 'http://www.baidu.com/'

#url代表的是下載的路徑，filename文件的名字
urllib.request.urlretrieve(url_page, 'baidu.html')

#下載影片 
 
# url_vedio = 'https://www.youtube.com/watch?v=298Fo2EKY4g&t=113s'
# urllib.request.urlretrieve(url_vedio, 'video.mp4') 


