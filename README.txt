===========
Sort-Image
===========

Sort-Image provides the ImageSorter class. You can use it to sort the pixels in an 
image by calling methods on that class.  Typical usage
often looks like this::

    #!/usr/bin/env python

    from sortpixels import ImageSorter

    image = ImageSorter("input.png")
    new_image = image.sortimage()
    new_image.save("output.png")

Documentation
--------------

You can see the documentation by checking out the docs/ directory included with this package. Enjoy!

Contributors
-------------

1. Matthew Edelen (Gihub Username mteam88)