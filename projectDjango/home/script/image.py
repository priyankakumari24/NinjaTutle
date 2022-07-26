import sys
from PIL import Image, ImageFilter, ImageEnhance

image_fullpath = sys.argv[1]
image_name = sys.argv[2]

img = Image.open(str(image_fullpath))
img_save_path = image_fullpath.replace(image_name, "temp.png")


blur = img.filter(ImageFilter.MedianFilter(size=7))
edges1 = blur.filter(ImageFilter.EDGE_ENHANCE_MORE)
edges2 = edges1.filter(ImageFilter.EDGE_ENHANCE)
color_quantize = edges2.quantize(25).save(img_save_path)


print('/Media/temp.png')
