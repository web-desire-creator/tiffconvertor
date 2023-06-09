import os
from os import listdir
from PIL import Image
import shutil
import cv2

i=1
url = os.getcwd()


dir = url+"\\tiff"
if not os.path.exists(dir): # if the directory does not exist
    os.makedirs(dir) # make the directory
else: 
    shutil.rmtree(dir)
    os.makedirs(dir)



for images in os.listdir(url):
    if (images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith(".png")):
        fileName = os.path.splitext(images)
        img_jpg=Image.open(url+"\\"+images)
        rgb=img_jpg.convert("RGB")
        rgb.save(url+"\\tiff\\"+fileName[0]+".tiff")
        image = cv2.imread(dir+"\\"+fileName[0]+".tiff")
        cv2.imwrite(dir+"\\"+fileName[0]+".tiff", image, params=(cv2.IMWRITE_TIFF_COMPRESSION, 8))
        file_name = dir+"\\"+fileName[0]+".tiff"
        file_stats = os.stat(file_name).st_size/1024
        if(file_stats>50):
            while((file_stats/(0.8*0.8))>40):
                im = Image.open(dir+"\\"+fileName[0]+".tiff")
                resized_im = im.resize((round(im.size[0]*0.8), round(im.size[1]*0.8)))
                resized_im.save(dir+"\\"+fileName[0]+".tiff")
                file_stats=file_stats*0.8*0.8
            i=i+1
        else:
            i=i+1
