import cv2
import numpy as np
import random

img = cv2.imread('colorcolor.jpg')
# print(type(img))
# print(img.shape)

# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [255, 0, 0]

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [0, 255, 0]

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [0, 0, 255]

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]



newimg = img[200:500, 200:500]

cv2.imshow('img', img)
cv2.imshow('newimg', newimg)
cv2.waitKey(0)