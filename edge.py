import cv2
import matplotlib.pyplot as plt
im = cv2.imread('flower.jpeg.jpeg')
edges = cv2.canny(im,100,300)
plt.imshow(edges)
plt.show()