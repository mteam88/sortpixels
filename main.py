from src import ImageSorter

i = ImageSorter("/workspace/sort-image/sort-image/test-images/monalisa.jpeg")
output = i.sortimage()

output.save('output.png')