import os, sys, io
from PIL import Image




print(sys.argv)

image_path = sys.argv[1]
crop_size = int(sys.argv[2])
img = Image.open(image_path)
print(image_path, crop_size)
image_width, image_height = img.size
n = 0
for x in range(0, image_width, crop_size):
    for y in range(0, image_height, crop_size):
        new_image = img.crop((x,y,x+crop_size,y+crop_size))
        if len(new_image.getcolors()) > 1:
            new_image.save(image_path.split('.')[0]+"_{}".format(n)+'.png')
            n += 1


