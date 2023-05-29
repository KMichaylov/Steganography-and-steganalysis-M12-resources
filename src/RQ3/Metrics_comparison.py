import cv2
from tabulate import tabulate
import os

# TODO: Create new dataset including at least 2 other different sizes and analyse the results.
# Ask Dipti for other sizes.
columns = ["Name", "Size", "Dimensions" "Color", "Entropy", "PSNR"]
folder_location = "D:\Study Materials\Year 3 (2022-2023)\Module " \
                  "12\Resources\Experiment_code\Steganography-and-steganalysis-M12-resources\images\RQ3-dataset" \
                  "\Images512x512\F5\m1-images"
# Decide how to use the data, draw your intentions.
# The needed files are adjacent, so just compare them.
count = 0
data = []
images = os.listdir(folder_location)
os.chdir(folder_location)
current_psnr = 0
for i in range(0, len(images) - 1):
    img_location = "D:\Study Materials\Year 3 (2022-2023)\Module " \
                   "12\Resources\Experiment_code\Steganography-and-steganalysis-M12-resources\images\RQ3-dataset" \
                   "\Images512x512\F5\m1-images\{}".format(images[i])
    row = list()
    img1 = cv2.imread(images[i])
    img2 = cv2.imread(images[i + 1])
    print(img1.shape)
    row.append(images[i])
    row.append("%.2f" % (os.path.getsize(img_location)) + " B")
    row.append(str(img1.shape[0]) + "X" + str(img1.shape[1]))
    if "-g" in images[i]:
        row.append('grayscale')
    else:
        row.append('colourful')
    if count % 2 == 0:
        psnr = cv2.PSNR(img1, img2)
        current_psnr = psnr
    else:
        psnr = current_psnr
    count +=1
    row.append("Entropy still unknown")
    row.append(psnr)
    data.append(row)
print(tabulate(data, headers=columns, tablefmt="grid", showindex="always"))
