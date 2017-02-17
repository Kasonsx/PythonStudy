from PIL import Image,ImageDraw  
##我们已经知道图片大小  
new_img = Image.new('RGB', (320, 240))  
img = Image.open('cave.jpg')  
for x in range(0,640,2):  
    for y in range(0,480,2):  
            pixel = img.getpixel((x, y))  
            new_img.putpixel((x//2, y//2), pixel)  
new_img.show()
new_img.save('challenge11.jpg')