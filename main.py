import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import os

save_dir="images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',}

query=input("Enter Name of Person:")
response=requests.get(f"https://www.google.com/search?rlz=1C1CHBF_enIN1025IN1025&sxsrf=APwXEdc34GeOnpR2X8Y5ZAWBspz8gM7Qww:1687591153718&q={query}&tbm=isch&sa=X&ved=2ahUKEwiT5_j5rtv_AhWHXGwGHUUqA0QQ0pQJegQIDBAB&biw=1600&bih=781&dpr=1")


soup=(BeautifulSoup(response.content,"html.parser"))
image_tages=(soup.find_all("img"))

del image_tages[0]

image_data_mongo=[]
for i in image_tages:
    image_url=i['src']
    image_data=requests.get(image_url).content
    mydict={"index" : image_url,"image" : image_data}
    image_data_mongo.append(mydict)
    with open(os.path.join(save_dir,f"{query}_{image_tages.index(i)}.jpg"),"wb") as f:
        f.write(image_data)