# install an external module and use it to perform operation of your own interest
# Using matplotlib and pyplot module to reas and write images

import matplotlib.pyplot as plt
import matplotlib.image as matimg # matimg=matplotlib image

# use the raw string (prefix the string with 'r') to avoid issues with backslashes
img=matimg.imread(r'C:\gallary\WhatsApp Images\IMG-20230824-WA0007.jpg')
# to display the image
plt.imshow(img)
plt.axis('off') #  hide axis
plt.show()
