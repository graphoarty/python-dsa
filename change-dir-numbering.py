import os, sys
from shutil import move

folder = "/Users/apple/Desktop/Images/"

for x in range (1, 21):
    move(os.path.join(folder, str(x)) , os.path.join(folder, str(x - 1)))