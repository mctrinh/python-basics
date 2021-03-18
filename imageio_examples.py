# Dependencies
# 1. Python 3.5+
# 2. Numpy
# 3. Pillow

import imageio
import visvis as vv     # to visualize image data, can also use Matplotlib to show the images (pip install visvis)

# Make image gray
im = imageio.imread('imageio_ex1.jpg')
print(im.shape)
imageio.imwrite('imageio_ex1_gray.jpg', im[:, :, 0])

im = imageio.imread('imageio_ex2.jpg')
print(im.shape)
imageio.imwrite('imageio_ex2_gray.jpg', im[:, :, 0])

# If the image is a GIF
im = imageio.get_reader('imageio_ex3.gif')
for frame in im:
    print(frame.shape)         # Each frame is a numpy matrix

# Read from fancy sources: filenames, file objects, http, zipfiles, bytes
im = imageio.imread('http://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png')
vv.imshow(im)
imageio.imwrite('imageio_ex_http.jpg', im)

# Grab screenshot or image from the clipboard
im_screen = imageio.imread('<screen>')
imageio.imwrite('imageio_ex_screen.jpg', im_screen)
im_clipboard = imageio.imread('<clipboard>')
# imageio.imwrite('imageio_ex_clip.jpg', im_clipboard)


# MORE EXAMPLES CAN BE FOUND AT
# https://imageio.readthedocs.io/en/stable/examples.html