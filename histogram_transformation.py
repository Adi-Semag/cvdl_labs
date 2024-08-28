#bad contrast imageimport numpy as np
import numpy as np
import cv2

img = cv2.imread("E:\\5th Sem\\CVDL\\images\\darker_image.png",cv2.IMREAD_GRAYSCALE)
newimg = np.zeros((img.shape[0],img.shape[1]), dtype = img.dtype)

mini = np.min(img)
maxi = np.max(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        newimg[i][j] = np.clip(((img[i][j] - mini)*255) / (maxi-mini),0,255)

cv2.imshow('imge',img)
cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows
