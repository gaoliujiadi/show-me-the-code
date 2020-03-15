#findTheText.py
from bs4 import BeautifulSoup
htmlStr = open('theHTML.html','r',encoding='utf-8').read()
htmlSoup = BeautifulSoup(htmlStr,"html.parser")
htmlP = htmlSoup.find('p')
Text = ''
for htmlPChild in htmlP.children:
    htmlPChildLs = str(htmlPChild).split('\n')
    htmlPChild = ''.join(htmlPChildLs)
    Text = Text + htmlPChild
htmlP = BeautifulSoup(Text,'html.parser')
text = ''
for P in htmlP.children:
    if P.string == None:
        continue
    else:
        text = text + P.string + '\n'
print(text)