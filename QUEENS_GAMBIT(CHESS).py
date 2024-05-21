from PIL import Image
from itertools import chain

# Create a new RGB image with dimensions 256x256
img = Image.new('RGB', (256, 256))

# Define ranges for x and y coordinates
ranges = [range(1, 32), range(64, 96), range(128, 160), range(192, 224)]
ranges_alt = [range(32, 64), range(96, 128), range(160, 192), range(224, 256)]

# Iterate through the ranges and set the pixels to white
for y in chain(*ranges, *ranges_alt):
    for x in chain(*ranges, *ranges_alt):
        img.putpixel((x, y), (255, 255, 255))

# Display the image
img.show()