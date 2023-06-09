import cv2
from tabulate import tabulate
import os
import csv
import numpy as np
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio

images_root_location = os.path.join("..", "..", "images", "RQ3-dataset", "Images512x512")
os.chdir(images_root_location)
image_dataset_names = ["F5", "Outguess", "Steghide"]
steganography_images_folder = ["m1-images", "m2-images", "m3-images", "m4-images", "m5-images"]
columns = ["Name", "Size", "Dimensions", "Color", "MSE", "PSNR"]
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
        location_for_results = os.path.join("..", "..", "..", "..", "..", "results", "RQ3",
                                            '{}-{}.csv'.format(image_dataset, steganograpy_dataset))
        with open(location_for_results, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Size", "Dimensions", "Color", "MSE", "PSNR"])
            for i in range(0, len(images)):
                path_to_image = os.path.join(os.getcwd(), images[i])
                img_location = "{}".format(path_to_image)
                row = list()
                # Only different for last item
                if i == len(images) - 1:
                    img1 = cv2.imread(images[i])
                    row.append(images[i])
                    row.append("%.2f" % (os.path.getsize(img_location)) + " B")
                    row.append(str(img1.shape[0]) + "X" + str(img1.shape[1]))
                    if "-g" in images[i]:
                        row.append('grayscale')
                    else:
                        row.append('colourful')
                    mse = current_mse
                    psnr = current_psnr
                    count += 1
                    row.append(mse)
                    row.append(psnr)
                    data.append(row)
                    writer.writerow(row)
                else:
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
                        mse = mean_squared_error(img1, img2)
                        psnr = peak_signal_noise_ratio(img2, img1)
                        current_psnr = psnr
                        current_mse = mse
                    else:
                        mse = current_mse
                        psnr = current_psnr
                    count += 1
                    row.append(mse)
                    row.append(psnr)
                    data.append(row)
                    writer.writerow(row)
            print(tabulate(data, headers=columns, tablefmt="grid", showindex="always"))
            new_path = os.path.join("..")
            os.chdir(new_path)
    new_path = os.path.join("..")
    os.chdir(new_path)
