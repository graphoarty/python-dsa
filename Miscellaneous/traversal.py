import os
import sys
from shutil import copy, move
from PIL import Image

rootdir = "/Users/apple/Desktop/RadiusXBKC/"

size = 4096, 2048

for root, subdirs, files in os.walk(rootdir):
    for f in files:

        filepath = os.path.join(root, f)

        if(filepath.endswith('.jpg')):
            im = Image.open(filepath)
            im = im.resize(size, Image.LANCZOS)
            im.save(filepath)

        if(filepath.endswith('.png')):
            im = Image.open(filepath)
            im = im.resize(size, Image.LANCZOS)
            im.save(filepath)