import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
import numpy as nump

# leer en la imagen e imprime
image = mpimg.imread('test.jpg')
print('this image is: 'type(image),'with dimensions:',image.shape)

#Grab the x and y and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

red_threshold = 0 
green_threshold = 0
blue_threshold = 0 
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# pixeles debajo del threshold calculados

thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
color_select[thresholds] = [0,0,0]

# imprime las imagenes

plt,imshow(color_select)
plt.show()
