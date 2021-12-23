from PIL import Image, ImageFilter

img = Image.open('../images/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")
crooked = filtered_img.rotate(84)
crooked.save("crookedPika.png","png")
resize = filtered_img.resize((1900 ,720))
resize.save('largePika.png', 'png')
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save('croppedPika.png', 'png')

#keeps aspect ratio
img2 = Image.open('../images/astro.jpg')
print(img2.size)
img2.thumbnail((400,400))
img2.save('smallastro.png', 'png')

