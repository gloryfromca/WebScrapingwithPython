import pdb
# pdb.set_trace()
from PIL import Image,ImageFilter 
import subprocess

def clean_gray(path):
    img=Image.open(path)
    img=img.point(lambda x:0 if x<143 else 255)
    new_path=path.split(".")[0]+'_clean.'+path.split(".")[1]
    img.save(new_path)
    return new_path

def tesseract_print(path):
    subprocess.call(['tesseract',path,"output"])
    output=open("output.txt")
    try:
        print(output.read())
    finally:
        output.close()

path="2.png"
new_path=clean_gray(path)
tesseract_print(new_path)

