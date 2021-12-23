import sys
import os
from PIL import Image

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

print(jpg_folder, png_folder)

if not (os.path.exists(png_folder)):
    os.makedirs(png_folder)

#Grab each image
for filename in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{filename}')
    remove_extension = os.path.splitext(filename)[0]
    img.save(f'{png_folder}{remove_extension}.png', 'png')
    print('Image converted')