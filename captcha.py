from PIL import Image
import sys
sys.setrecursionlimit(10000)

im = Image.open("output.gif")

def finder(image, pointed, point):
    temp = []

    try:
        p = (point[0]+1, point[1])
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            im.putpixel(p, 227)

        p = (point[0], point[1]+1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0], point[1]-1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0]+1, point[1]+1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0]+1, point[1]-1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0]-1, point[1]+1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0]-1, point[1]-1)
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)

        p = (point[0]-1, point[1])
        pix = image.getpixel(p)
        if pix == 0:
            temp.append(p)
            pointed.append(p)
            image.putpixel(p, 227)
    except:
        pass

    for po in temp:
        finder(im, pointed, po)

count = 4
for y in range(im.size[1]):
  for x in range(im.size[0]):
    pix = im.getpixel((x, y))
    #Массив для черных точек
    pointed = []
    #Нашли черную точку
    if pix == 0:
        pointed.append((x, y))
        #закрашиваем точку, чтобы больше не встречалась
        im.putpixel((x, y), 227)
        #ищем все блиджайшие черные точки
        finder(im, pointed, (x, y))
        # если точек больше ста, то эти точки цифра
        if len(pointed) > 100:
            minx = maxx = pointed[0][0]
            miny = maxy = pointed[0][1]
            # Ищем границы цифры на рисунке
            for pix in pointed:
                if pix[0] > maxx:
                    maxx = pix[0]
                if pix[0] < minx:
                    minx = pix[0]

                if pix[1] > maxy:
                    maxy = pix[1]
                if pix[1] < miny:
                    miny = pix[1]

            #создаем картинку для этой буквы
            letter = Image.new("P", (maxx-minx+1,maxy-miny+1), 255)
            for pix in pointed:
                print("{} {} {} {}".format(pix[0],minx,pix[1],miny)+" x="+str(pix[0]-minx)+" y="+str(pix[1]-miny))
                letter.putpixel((pix[0]-minx, pix[1]-miny), 0)

            letter.save("letters/{}.gif".format(count))
            count -= 1
