import cv2
from tabulate import tabulate
import os
from os import listdir

columns = ["Size", "Dimension", "Color", "Entropy", "PSNR"]
folder_location = "D:\Study Materials\Year 3 (2022-2023)\Module " \
                  "12\Resources\Experiment_code\Steganography-and-steganalysis-M12-resources\images\RQ3-dataset" \
                  "\Images512x512\F5\m1-images"
# The needed files are adjacent, so just compare them.
images = os.listdir(folder_location)
os.chdir(folder_location)
for i in range(0, len(images) - 1, 2):
    img1 = cv2.imread(images[i])
    img2 = cv2.imread(images[i+1])
    psnr = cv2.PSNR(img1, img2)
    print(images[i], images[i+1])
    print(psnr)
