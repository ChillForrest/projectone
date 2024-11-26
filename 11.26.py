import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image=cv.imread('')

hist,bins=np.histogram(image.flatten(),256,[0,256])

cdf=hist.cumsum()
cdf_normalized=cdf*hist.max()/cdf.max()
equalized_image=cdf_normalized[image]

plt.subplot(121),plt.imshow(iamge,cmap='gray')
plt.title('image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(equalized_image,cmap='gray')
plt.title('equalized_image'),plt.xticks([]),plt.yticks([])

plt.figure()
plt.subplot(121),plt.plot(hist)
plt.title('original')
plt.subplot(122),plt.plot(cdf_normalized)

plt.title('equalized_image')
plt.show