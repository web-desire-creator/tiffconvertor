import os
from os import listdir
from PIL import Image
import shutil
import cv2

i=1
# url = input("Add path of first file: ")
url = os.getcwd()


dir = url+"\\tiff"
if not os.path.exists(dir): # if the directory does not exist
    os.makedirs(dir) # make the directory
else: 
    shutil.rmtree(dir)
    os.makedirs(dir)



for images in os.listdir(url):
    if (images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith(".png")):
        print(images)
        img_jpg=Image.open(url+"\\"+images)
        rgb=img_jpg.convert("RGB")
        rgb.save(url+"\\tiff\\"+str(i)+".tiff")
        image = cv2.imread(dir+"\\"+str(i)+".tiff")
        cv2.imwrite(dir+"\\"+str(i)+".tiff", image, params=(cv2.IMWRITE_TIFF_COMPRESSION, 8))
        print("Image Compressed Successfully")
        im = Image.open(dir+"\\"+str(i)+".tiff")
        resized_im = im.resize((round(im.size[0]*1), round(im.size[1]*1)))
        resized_im.save(dir+"\\"+str(i)+".tiff")
        i=i+1
