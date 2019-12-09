import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread('hellur.png')

blur = cv.GaussianBlur(img, (5,5), 0)
fin = cv.addWeighted(img, 1.5, blur, -0.5, 0, img);

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(fin),plt.title('Final')
plt.xticks([]), plt.yticks([])
plt.show()
