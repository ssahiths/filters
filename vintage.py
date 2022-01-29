import cv2
import numpy as np
from matplotlib import pyplot as plt
im = cv2.imread('house.jpeg.jpeg')
rows, cols = im.shape[:2]
# create a gaussian filter
Kernel_x = cv2.getGaussianKernel(cols,200)
Kernel_y = cv2.getGaussianKernel(rows,200)
Kernel = Kernel_y * Kernel_x.T
filter = 255 * Kernel / np.linalg.norm(Kernel)
vintage_im = np.copy(im)
# for each channel in the input image, we will apply the above filter
for i in range(3):
    vintage_im[:,:,i] = vintage_im[:,:,i] * filter      
plt.imshow(vintage_im) 
plt.show()
