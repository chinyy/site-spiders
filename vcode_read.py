# coding=utf-8

import os, sys
import pytesseract
import requests
from PIL import Image

# sudo pip install pytesseract
# sudo pip install Pillow
# sudo brew install tesseract

def downloadImageFile(imgUrl):  
    local_filename = imgUrl.split('/')[-1]  
    r = requests.get(imgUrl, stream=True)
    img_filename = os.path.abspath(os.curdir)+'/'+local_filename
    with open(img_filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk:
                f.write(chunk)  
                f.flush()  
        f.close()  
    return img_filename

def get_vcode(img):
    image = Image.open(img)
    vcode = pytesseract.image_to_string(image)
    return vcode

if __name__ == '__main__':
    img = downloadImageFile("http://zzfws.bjjs.gov.cn/enroll/checkcode/ag3e6fm94ehqbubk.jpg")
    print get_vcode(img)
