from sortimage import ImageSorter

i = ImageSorter(filename="./sort-image/test-images/monalisa.jpeg")
output = i.sortimage()
output.save('./output.png')