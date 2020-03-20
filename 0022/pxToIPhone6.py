#pxToIPhone6.py
#750*1334
#我认为小于iPhone6像素即可，不必全都一样

from PIL import Image
import glob
import os.path as op

def cut(im,path):
    if im.size[0] < im.size[1]:#宽<高，竖着
        ratio = px[0] / im.size[0] 
        after = (im.size[0] * ratio,im.size[1] * ratio)
        im.thumbnail(after)
        print(im.size)
        im.save(path)
    else:
        ratio = px[1] / im.size[1]
        after = (im.size[0] * ratio,im.size[1] * ratio)
        im.thumbnail(after)
        print(im.size)
        im.save(path)

if __name__ == '__main__':
    im = glob.glob(r'original\*.jpg')
    px = (750,1334)
    for i in im:
        path = 'after' + '\\' + op.basename(i)
        img = Image.open(i)
        cut(img,path)