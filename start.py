from PIL import Image
from operator import itemgetter

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

im = Image.open("image.jpg")
im = im.convert("P")

im = change_contrast(im, 100)

############################################################
his = im.histogram()

values = {}

for i in range(256):
  values[i] = his[i]

for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
  print(j,k)

#########################################################
im2 = Image.new("P",im.size,255)

temp = {}

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y, x))
    temp[pix] = pix
    if pix == 0: # these are the numbers to get
      im2.putpixel((y,x),0)

im2.save("output.gif")