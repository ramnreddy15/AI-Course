import sys; args = sys.argv[1:]
from PIL import Image; img = Image.open(args[0])
from re import I
import PIL
# import urllib.request
import random
# import tkinter as tk
# from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

def random_means(k):
   means = []
   while(len(means) < k):
       temp = (random.uniform(0,255), random.uniform(0,255), random.uniform(0,255))
       if temp not in means: means.append(temp)
   return means

def dist(col, means):
   r, g, b = col
   return (means[0]-r)**2+(means[1]-g)**2+(means[2]-b)**2 

def createClusters(img, pix, count_buckets, move_count, means, count):
    clusters = [[] for i in range(len(means))]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
           temp = []
           for m in means:
            temp.append(dist(pix[i,j], m))
           minV = min(temp)
           clusters[temp.index(minV)].append(pix[i,j])
   #  print("count buckets", count_buckets)
    for i in range(len(clusters)):
       
       move_count[i] = abs(len(clusters[i]) - count_buckets[i])
       count_buckets[i] = len(clusters[i])
       r, g, b = 0, 0, 0
       if len(clusters[i]) > 0:
         for color in clusters[i]:
            r+=color[0]
            g+=color[1]
            b+=color[2]

         r/=len(clusters[i])
         g/=len(clusters[i])
         b/=len(clusters[i])
       means[i] = (r,g,b)

    return count_buckets, move_count, means

def distinct_pix_count(img, pix):
   cols = {pix[0,0]:0}
   max_col, max_count = pix[0, 0], 0
   for i in range(img.size[0]):
      for j in range(img.size[1]):
         if pix[i,j] in cols.keys():
            cols[pix[i,j]] = cols[pix[i,j]]+1
         else:
            cols[pix[i,j]] = 0
         if cols[pix[i,j]] > cols[max_col]:
            max_col = pix[i,j]

   for i in cols.keys():
      if cols[i] > max_count:
         max_count = cols[i]

   return len(cols.keys()), max_col, max_count

def check_move_count(mc):
   if sum(mc) > 0:
      return True
   else:
      return False

def update_picture(img, pix, means):
   for i in range(img.size[0]):
        for j in range(img.size[1]):
           temp = []
           for m in means:
            temp.append(dist(pix[i,j], m))
           minV = min(temp)
           pix[i,j] = tuple([int(k) for k in means[temp.index(minV)]])
   return pix

def floodFill(i,j,img,pix,color):
   if i<0 or j<0 or i>=img.size[0] or j>=img.size[1]: return pix
   if pix[i,j] != color: return pix
   if(pix[i,j] == color): pix[i,j] = (-1,-1,-1)
   floodFill(i+1,j,img,pix,color)
   floodFill(i+1,j+1,img,pix,color)
   floodFill(i+1,j-1,img,pix,color)
   floodFill(i,j+1,img,pix,color)
   floodFill(i-1,j+1,img,pix,color)
   floodFill(i-1,j-1,img,pix,color)
   floodFill(i-1,j,img,pix,color)
   floodFill(i,j-1,img,pix,color)
   return pix
def countRegions(img, pix, means):
   regions = [0 for i in range(len(means))]
   for i in range(img.size[0]):
        for j in range(img.size[1]):
           if pix[i,j] != (-1,-1,-1):
               temp = []
               for m in means:
                temp.append(dist(pix[i,j], m))
               minV = min(temp)
               regions[temp.index(minV)] = regions[temp.index(minV)]+1
               pix = floodFill(i,j,img,pix,pix[i,j])
               
   return regions

def main():
   k = int(sys.argv[1])
   file = sys.argv[2]
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   
   
   
#    img_tk = ImageTk.PhotoImage(img)
#    lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   
   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = random_means(k)
#    print ('random means:', means)
   count = 1
   while check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = createClusters(img, pix, count_buckets, move_count, means, count)
#       print("diff", count, ":", move_count)
#       if count == 2:
#          print ('first means:', means)
#          print ('starting sizes:', count_buckets)
   print("here:")
   print ('Final means:')
   for i in range(len(means)):
      print (str(i+1) + ':', means[i], '=>', count_buckets[i]) 
   pix = update_picture(img, pix, means)  # region_dict can be an empty dictionary
      print("diff", count, ":", move_count)
      if count == 2:
         print ('first means:', means)
         print ('starting sizes:', count_buckets)
   pix = update_picture(img, pix, means)  # region_dict can be an empty dictionary
   print ('Final sizes:', count_buckets)
      
#    img_tk2 = ImageTk.PhotoImage(img)
#    lbl = tk.Label(window, image = img_tk2).pack()  # display the image at window
   
   img.save('kmeans/2023rreddy.png', 'PNG')  # change to your own filename 
   print ('Region counts:', countRegions(img, pix,means))
#    img.save('2023rreddy.png', 'PNG')  # change to your own filename
#    window.mainloop()
#    img.show()


if __name__ == '__main__': 
   main()

# Ram Reddy, 5, 2023