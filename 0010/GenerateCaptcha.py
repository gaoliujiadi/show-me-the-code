#GenerateCaptcha.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
def ranChar():
    return chr(random.randint(65, 90))

w = 60 * 4
h = 60
def ranColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def ranColor1():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

image = Image.new('RGB', (w, h), (255, 255, 255))
font = ImageFont.truetype('AGENCYB.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=ranColor())
for t in range(4):
    draw.text((60 * t + 10, 10), ranChar(), font=font, fill=ranColor1())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')