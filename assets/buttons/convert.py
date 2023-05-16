import pickle
from PIL import Image
from sys import argv

print(argv)
def convert_pxo_to_png(pxo_file_path, png_file_path):
    with open(pxo_file_path, 'rb') as file:
        data = pickle.load(file)

    width = data['width']
    height = data['height']
    pixel_data = data['pixels']

    image = Image.new('RGBA', (width, height))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            pixel_color = tuple(pixel_data[y * width + x])
            pixels[x, y] = pixel_color

    image.save(png_file_path, 'PNG')

convert_pxo_to_png(argv[1], argv[2])
