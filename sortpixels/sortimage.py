from PIL import Image
import numpy as np
from functools import reduce
import logging

class ImageSorter():
    def __init__(self, filename="input.png", keyfunc=sortimage):
        '''
        Initiates an ImageSorter object. 
        parameters:
        filename: path to a file, defaults to input.png, can be any file type supported by Pillow
        keyfunc: defaults to sortimage(), should be a function that can be used in a sort method. 
            it will be passed "pixel," a tuple of rgb values in the form (R, G, B). E.g: (127,3,12)
            and it could return an integer. Check out the sort() method documentation to find out more.
            The default sortimage keyfunc sorts the image by the sum of the rgb values.
        '''
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
        logging.info(f"pixel: {pixel}")
        logging.info(f"sum: {sum(list(pixel))}")
        return sum(list(pixel))
    
    def _to_matrix(self, flatlist, rowl):
        return [flatlist[i:i+rowl] for i in range(0, len(flatlist), rowl)]