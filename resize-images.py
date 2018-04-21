import os, sys
from PIL import Image

folder = "/Users/apple/Desktop/Radius\ X\ BKC/"

size = 4096, 2048

for root, dirs, files in os.walk(folder):
    
    print('Working')

    for name in files:
        print(os.path.join(root, name))
        # im = Image.open(image)
        # im = im.resize(size, Image.LANCZOS)
        # im.save(os.path.join(folder, os.path.join(root, name)))