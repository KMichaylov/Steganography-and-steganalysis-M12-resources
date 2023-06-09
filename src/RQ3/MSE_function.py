# import cv2
# import numpy as np
#
#
# # The code is from GeeksForGeeks: https://www.tutorialspoint.com/how-to-compare-two-images-in-opencv-python
# def MSE(cover_image, stego_image):
#     h, w, _ = cover_image.shape
#     diff = cv2.subtract(cover_image, stego_image)
#     err = np.sum(diff ** 2)
#     mse = err / (float(h * w))
#     return mse
