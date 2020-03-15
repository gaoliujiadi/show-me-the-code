#findTheLinks.py
from bs4 import BeautifulSoup
htmlStr = open('theHTML.html','r',encoding='utf-8').read()
htmlSoup = BeautifulSoup(htmlStr,"html.parser")
#print(htmlSoup)
links = htmlSoup.find_all(attrs={'href':True})
for link in links:
    if link.attrs['href'][:4] == 'http':
        print(link.attrs['href'])