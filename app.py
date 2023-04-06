import os
from os import listdir
from PIL import Image

i=1
folder_dir=os.getcwd()
for images in os.listdir(folder_dir):
    if (images.endswith(".jpg") or images.endswith(".jpeg")):
        img_jpg=Image.open(images)
        img_jpg=img_jpg.resize((128,128),Image.ANTIALIAS)
        rgb=img_jpg.convert("RGB")
        rgb.save(os.getcwd()+"/tiff/"+str(i)+".tiff")
        i=i+1
