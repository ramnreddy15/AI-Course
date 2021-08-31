import PIL
from PIL import Image
import urllib.request
import io, sys
print (PIL.PILLOW_VERSION)
URL = sys.argv[1] # URL is a link of a file
f = io.BytesIO(urllib.request.urlopen(URL).read())
img = Image.open(f)
print (img.size)
pix = img.load()
print (pix[2, 5])
img = img.show()

# image: https://cdn.jpegmini.com/user/images/pufffin_blurred.jpg