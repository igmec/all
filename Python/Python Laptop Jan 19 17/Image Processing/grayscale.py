from PIL import Image

img = Image.open("C:\\Users\\Igor\\Desktop\\gray_tiny.png")

w,h = img.size

new = Image.new('RGB',img.size)

for x in range(h):
    for y in range(w):
        pix = img.getpixel((y,x))
        r,g,b = pix
        gray = int((r+g+b)/3)
        blkThrsh = 200

        if gray >= blkThrsh:
            gray = 255
            new.putpixel((y,x),(gray,gray,gray))
        else:
            gray = 0
            new.putpixel((y,x),(gray,gray,gray))


new.save("gray_tiny2.png")
