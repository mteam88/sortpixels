from sortpixels import ImageSorter

i = ImageSorter(filename="input.jpeg")
output = i.sortimage()
output.save('./output.png')