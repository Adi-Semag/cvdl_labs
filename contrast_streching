import numpy as np
import cv2

img = cv2.imread("E:\\5th Sem\\CVDL\\images\\color\\lena_color.png",cv2.IMREAD_GRAYSCALE)
newimg = np.zeros((img.shape[0],img.shape[1]), dtype = img.dtype)

rmin = np.min(img)
rmax = np.max(img)
print("Range is: ",rmin,"to",rmax)
smin = int(input("Enter lower bound: "))
smax = int(input("Enter upper bound: "))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        newimg[i][j] = (((img[i][j] - rmin) * (smax-smin)) / (rmax - rmin) + smin)


cv2.imshow('imge',img)
cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows
