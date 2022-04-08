from PIL import Image
import numpy as np
from functools import reduce

class ImageSorter():
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open(filename)
        pixels = list(self.im.getdata())
        width, height = self.im.size
        self.pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        self.pixels = reduce(lambda z, y :z + y, self.pixels)

    def sortimage(self):
        self.sortpixels(self.pixels)
        matrixed = self._to_matrix(self.pixels, self.im.size[0]) # Maybe [1]
        
        # Convert the pixels into an array using numpy
        array = np.array(matrixed, dtype=np.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        return new_image
    
    def sortpixels(self, pixels):
        self.pixels.sort(key=self._tuplesum)

    def _tuplesum(self, pixel):
        #print(f"pixel: {pixel}")
        #print(f"sum: {sum(list(pixel))}")
        return sum(list(pixel))
    
    def _to_matrix(self, flatlist, rowl):
        return [flatlist[i:i+rowl] for i in range(0, len(flatlist), rowl)]