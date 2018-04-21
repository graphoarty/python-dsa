import os, sys
from PIL import Image

width = 4096
height = 2048

folder = "/Users/apple/Desktop/Radius\ X\ BKC/"

leftImagePath = os.path.join(folder, "left.jpg")
rightImagePath = os.path.join(folder, "right.jpg")

z = 5
counter = 0
while z > 0:

    factor  = 2 * counter
    
    if factor == 0:
        factor = 1

    new_width = width / factor
    new_height = height / factor

    size = new_width, new_height

    im = Image.open(leftImagePath)
    im = im.resize(size, Image.LANCZOS)
    im.save(os.path.join(folder, str(z) + "_left.jpg"))

    im = Image.open(rightImagePath)
    im = im.resize(size, Image.LANCZOS)
    im.save(os.path.join(folder, str(z) + "_right.jpg"))

    counter = counter + 1
    z = z - 1

# for x in range(1, 21):

#     leftImagePath = os.path.join(os.path.join(folder, str(x)), "left.jpg")
#     rightImagePath = os.path.join(os.path.join(folder, str(x)), "right.jpg")

#     z = 5
#     counter = 0
#     while z > 0:

#         factor  = 2 * counter
        
#         if factor == 0:
#             factor = 1

#         new_width = width / factor
#         new_height = height / factor

#         size = new_width, new_height

#         im = Image.open(leftImagePath)
#         im = im.resize(size, Image.BILINEAR)
#         im.save(os.path.join(os.path.join(folder, str(x)), str(z) + "_left.jpg"))

#         im = Image.open(rightImagePath)
#         im = im.resize(size, Image.BILINEAR)
#         im.save(os.path.join(os.path.join(folder, str(x)), str(z) + "_right.jpg"))

#         counter = counter + 1
#         z = z - 1