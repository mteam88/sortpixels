from sortpixels import ImageSorter

i = ImageSorter(filename="input.py")
output = i.sortimage()
output.save('./output.png')