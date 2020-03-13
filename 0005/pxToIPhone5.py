#pxToIPhone5.py
#640*1360
#我认为小于iPhone5像素即可，不必全都一样

from PIL import Image
import glob
import os.path as op

im = glob.glob(r'original\*.jpg')

def cut(im,path):
    if im.size[0] < im.size[1]:#宽<高，竖着
        ratio = 640 / im.size[0] 
        after = (im.size[0] * ratio,im.size[1] * ratio)
        im.thumbnail(after)
        print(im.size)
        im.save(path)
    else:
        ratio = 1360 / im.size[1]
        after = (im.size[0] * ratio,im.size[1] * ratio)
        im.thumbnail(after)
        print(im.size)
        im.save(path)

def main():
    for i in im:
        path = 'after' + '\\' + op.basename(i)
        img = Image.open(i)
        cut(img,path)

main()

#print(type(op.basename(im[0])))