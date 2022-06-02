# Day 1 Note
import PIL
from PIL import Image
import urllib.request
import io, sys
#print (PIL.PILLOW_VERSION)
# URL = &#39;http://www.w3schools.com/css/trolltunga.jpg&#39;
# #URL = sys.argv[1]
# f = io.BytesIO(urllib.request.urlopen(URL).read())
import tkinter as tk
from PIL import Image, ImageTk # Place this at the end (to avoid any conflicts/errors)
window = tk.Tk()
#window.geometry(&quot;500x500&quot;) # (optional)
imagefile = "cute_dog.jpg"
img = ImageTk.PhotoImage(Image.open(imagefile))
lbl = tk.Label(window, image = img).pack()
img2 = Image.open(imagefile)
img4 = Image.open(imagefile)
print (img2.size) # a tuple of (# of rows, # of cols)
pix = img2.load()
pix2 = img4.load()
print (pix[2, 5]) # a tuple of (r, g, b)
def chrome(color):
    if color  < (255 // 3): return 0
    elif color > (255 // 3 * 2): return 255
    else: return 127

def negate(color):
    return 255-color

def sepia(r,g,b):
    tr = 0.393*r + 0.769*g + 0.189*b
    tg = 0.349*r + 0.686*g + 0.168*b
    tb = 0.272*r + 0.534*g + 0.131*b

    if tr > 255: r= 255 
    else: r=tr


    if tg > 255: g= 255 
    else: g=tg

    
    if tb > 255: b= 255 
    else: b=tb
    return int(r),int(g),int(b)

def grayscale(r,g,b):
    avg = (r+g+b)/3
    return int(avg),int(avg),int(avg)

def mirror(img):
    for x in range(img2.size[0]):
        for y in range(img2.size[1]):
            r, g, b = pix2[img2.size[0]-1-x, img2.size[1]-1-y]
            # r,g,b = grayscale(r,g,b)
            pix[x, y] = (r,g,b)

mirror(img2)
#img2.show()
img3 = ImageTk.PhotoImage(img2)
lbl2 = tk.Label(window, image = img3).pack()
window.mainloop()