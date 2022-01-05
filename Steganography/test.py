import numpy as np
import cv2

img = cv2.imread('/Users/davidhuang/Python/HardwareSecurity/Steganography/car.jfif')
px = img[80,99]

print(px)
print(img.shape)
print(img.size)
x = img.shape[0]
y = img.shape[1]
z = img.shape[2]
print(x)
print(y)
print(z)



