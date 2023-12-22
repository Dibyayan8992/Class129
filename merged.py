import csv

data_1 = []
data_2 = []

with open('final.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data_1.append(row)
with open('archive_dataset_sorted.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data_2.append(row)

header_1 = data_1[0]
header_2 = data_2[0]

planet_data1 = data_1[1:]
planet_data2 = data_2[1:]

header = header_1 + header_2
planet_data = []
for index, row in enumerate(planet_data1):
    planet_data.append(row + planet_data2[index])

with open('merged_dataset.csv', 'w', newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(planet_data)