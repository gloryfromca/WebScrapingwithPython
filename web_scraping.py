import pdb
# pdb.set_trace()
from PIL import Image,ImageFilter 
cat=Image.open("cat.jpg")
blurrycat=cat.filter(ImageFilter.GaussianBlur)
blurrycat.save("cat_blur.jpg")
blurrycat.show()


