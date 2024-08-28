import numpy as np
import cv2

img = cv2.imread("E:\\5th Sem\\CVDL\\images\\color\\lena_color.png",cv2.IMREAD_GRAYSCALE)
newimg = np.zeros((img.shape[0],img.shape[1]), dtype = img.dtype)

g = 0.5
c = 1

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n = img[i][j] / 255
        newimg[i][j] = np.clip(c * (n ** g) * 255,0,255)

cv2.imshow('imge',img)
cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows
