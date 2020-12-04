import os
import sys
from PIL import Image

lines = os.listdir('images')

images = [Image.open(i) for i in lines]

print(images)