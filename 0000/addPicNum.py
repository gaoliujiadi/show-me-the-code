#000_addPicNum.py

from PIL import Image,ImageDraw,ImageFont

im = Image.open('original.jpg')
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('AGENCYB.TTF',150)
draw.text((450,10),'22',fill='red',font=font)
im.save('changed.jpg')
