#spiderThePic.py
import requests
from bs4 import BeautifulSoup
import os
r = requests.get('http://tieba.baidu.com/p/2166231880')
soup = BeautifulSoup(r.text,'html.parser')
picTags = soup.find_all(attrs={'class':"BDE_Image"})
picLinks = []
if not os.path.exists('pic\\'):
    os.mkdir('pic\\')
for picLink in picTags:
    picLink1 = picLink.attrs['src']
    picLinks.append(picLink1)
    picHtml = requests.get(picLink1)
    #picHtml.encoding = picHtml.apparent_encoding
    pic = picHtml.content
    name = picLink1.split('/')[-1]
    with open('pic\\' + name,'wb',) as f:
        f.write(pic)
print('done')