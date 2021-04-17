import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/exists, otherwise create

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex,
# convert images to png
# save to the new folder
for filename in os.listdir(image_folder):
    filename_without_extension = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}/{filename}')
    img.save(f'{output_folder}/{filename_without_extension}.png', 'png')
print("all done")
