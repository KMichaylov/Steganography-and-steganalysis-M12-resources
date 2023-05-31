import cv2
from tabulate import tabulate
import os
from MSE_function import MSE
import numpy as np

# TODO: Sort the images alphabetically, to ensure that cover and stego are adjacent!
images_root_location = os.path.join("..", "..", "images")
os.chdir(images_root_location)
image_dataset_names = ["F5-dataset", "Outguess-dataset", "Steghide-dataset"]
steganography_images_folder = ["m1-images", "m2-images", "m3-images", "m4-images", "m5-images"]
columns = ["Name", "Size", "Dimensions" "Color", "MSE", "PSNR"]
for image_dataset in image_dataset_names:
    new_path = os.path.join(os.getcwd(), image_dataset)
    os.chdir(new_path)
    for steganograpy_dataset in steganography_images_folder:
        new_path = os.path.join(os.getcwd(), steganograpy_dataset)
        os.chdir(new_path)
        count = 0
        data = []
        images = os.listdir(os.getcwd())
        current_psnr = 0
        current_mse = 0
        for i in range(0, len(images) - 1):
            path_to_image = os.path.join(os.getcwd(), images[i])
            img_location = "{}".format(path_to_image)
            row = list()
            img1 = cv2.imread(images[i])
            img2 = cv2.imread(images[i + 1])
            row.append(images[i])
            row.append("%.2f" % (os.path.getsize(img_location)) + " B")
            row.append(str(img1.shape[0]) + "X" + str(img1.shape[1]))
            if "-g" in images[i]:
                row.append('grayscale')
            else:
                row.append('colourful')
            if count % 2 == 0:
                mse = MSE(img1, img2)
                psnr = cv2.PSNR(img1, img2)
                current_psnr = psnr
                current_mse = mse
            else:
                mse = current_mse
                psnr = current_psnr
            count += 1
            row.append(mse)
            row.append(psnr)
            data.append(row)
        print(tabulate(data, headers=columns, tablefmt="grid", showindex="always"))
        new_path = os.path.join("..")
        os.chdir(new_path)
    new_path = os.path.join("..")
    os.chdir(new_path)
