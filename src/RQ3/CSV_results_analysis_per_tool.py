import cv2
from tabulate import tabulate
import os
import csv
import pandas as pd
import numpy as np
from statistics import mean

images_root_location = os.path.join("..", "..", "results", "RQ3")
os.chdir(images_root_location)
image_dataset_names = ["F5", "Outguess", "Steghide"]
CSV_FILES = [["F5-m1-images.csv", "F5-m2-images.csv", "F5-m3-images.csv", "F5-m4-images.csv", "F5-m5-images.csv"],
             ["Outguess-m1-images.csv", "Outguess-m2-images.csv", "Outguess-m3-images.csv", "Outguess-m4-images.csv",
              "Outguess-m5-images.csv"],
             ["Steghide-m1-images.csv", "Steghide-m2-images.csv", "Steghide-m3-images.csv", "Steghide-m4-images.csv",
              "Steghide-m5-images.csv"]]

columns = ["Name", "Color", "Mean Stego Images Size", "Standard Deviation of Stego Images Sizes",
           "Non-Stego Size - Stego Image Size",
           "Mean Stego Images MSE",
           "Standard Deviation of Stego Images MSE",
           "MSE values for respective embeddings",
           "Mean PSNR", "Standard Deviation PSNR", "PSNR values for respective embeddings"
           ]

for i in range(0, 3):
    location_for_results = os.path.join("..", "RQ3_data_per_tool",
                                        '{}.csv'.format(CSV_FILES[i][0].split("-")[0]))
    df = pd.concat(map(pd.read_csv, CSV_FILES[i]))
    table_data = []
    with open(location_for_results, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for j in range(0, 31, 2):
            row = []
            elements = df.loc[j]
            name_of_file = elements['Name'].tolist()
            row.append(name_of_file[0])
            color_of_file = elements['Color'].tolist()
            row.append(color_of_file[0])
            list_of_sizes = elements['Size'].tolist()
            elements_with_only_numbers = [el.replace(" B", "") for el in list_of_sizes]
            elements_converted_to_numbers = [float(el) for el in elements_with_only_numbers]
            mean_size = np.mean(elements_converted_to_numbers)
            row.append(mean_size)
            standard_deviation_size = np.std(elements_converted_to_numbers)
            row.append(standard_deviation_size)
            non_stego_size = df.loc[j + 1]['Size'].tolist()[0].replace(" B", "")
            non_stego_size = float(non_stego_size)
            deviation_from_non_stego_size = [non_stego_size - x for x in elements_converted_to_numbers]
            row.append(deviation_from_non_stego_size)

            elements_converted_to_numbers_mse = [float(el) for el in elements['MSE'].tolist()]
            mean_mse = np.mean(elements_converted_to_numbers_mse)
            row.append(mean_mse)
            standard_deviation_mse = np.std(elements_converted_to_numbers_mse)
            row.append(standard_deviation_mse)
            # non_stego_mse = df.loc[j + 1]['MSE'].tolist()[0]
            # non_stego_mse = float(non_stego_mse)
            # deviation_from_non_stego_mse = [non_stego_mse - x for x in elements_converted_to_numbers_mse]
            row.append(elements_converted_to_numbers_mse)

            elements_converted_to_numbers_psnr = [float(el) for el in elements['PSNR'].tolist()]
            mean_psnr = np.mean(elements_converted_to_numbers_psnr)
            row.append(mean_psnr)
            standard_deviation_psnr = np.std(elements_converted_to_numbers_psnr)
            row.append(standard_deviation_psnr)
            # non_stego_psnr = df.loc[j + 1]['PSNR'].tolist()[0]
            # non_stego_psnr = float(non_stego_psnr)
            # deviation_from_non_stego_psnr = [non_stego_psnr - x for x in elements_converted_to_numbers_psnr]
            row.append(elements_converted_to_numbers_psnr)
            table_data.append(row)
            writer.writerow(row)
        print(tabulate(table_data, headers=columns, tablefmt="grid", showindex="always"))
