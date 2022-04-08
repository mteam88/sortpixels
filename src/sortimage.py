from PIL import Image

class ImageSorter():
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open(filename)
        pixels = list(im.getdata())
        width, height = im.size
        self.pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        print(pixels)