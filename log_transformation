import numpy as np
import cv2 
import math

img = cv2.imread("E:\\5th Sem\\CVDL\\images\\darker_image.png", cv2.IMREAD_GRAYSCALE)
newimg = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)

maxi = np.max(img)
print(maxi)
c = 255 / math.log(1 + maxi)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        newimg[i][j] = c * math.log(1 + img[i][j])

cv2.imshow('imge',img)
cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows
